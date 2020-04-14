"""
Views for the passwordreset Opal Plugin
"""
import datetime
import logging
from django.http import Http404
from django.urls import reverse
from django.conf import settings
from django.core.signing import TimestampSigner
from django.template.loader import render_to_string
from django.contrib.auth import login, get_user_model
from django.views.generic import RedirectView, FormView, TemplateView
from django.core.mail import send_mail
from . import forms

LOGIN_SALT = "login"
User = get_user_model()
logger = logging.getLogger(__name__)


class RequestReset(FormView):
    template_name = "passwordreset/send_email_link.html"
    form_class = forms.SendEmailForm

    def get_success_url(self):
        return reverse("check-email")

    def get_reset_link(self, user):
        signed_pk = TimestampSigner(salt=LOGIN_SALT).sign(user.pk)
        url = reverse("hash-login", kwargs={"signed_pk": signed_pk})
        return self.request.build_absolute_uri(url)

    def send_email(self, username):
        user = User.objects.get(username=username)
        absolute_url = self.get_reset_link(user)
        if settings.DEBUG:
            print("In production you would login with the url {}".format(absolute_url))
        else:
            send_mail(
                "{} password reset".format(settings.OPAL_BRAND_NAME),
                "Please reset your password by going to {}".format(absolute_url),
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                html_message=render_to_string(
                    "passwordreset/reset_email.html",
                    {
                        "brand_name": settings.OPAL_BRAND_NAME,
                        "user": user,
                        "url": absolute_url,
                    },
                ),
            )

    def form_valid(self, form, *args, **kwargs):
        self.send_email(form.cleaned_data["username"])
        return super().form_valid(form, *args, **kwargs)


class CheckYourEmailPage(TemplateView):
    template_name = "passwordreset/check.html"


class HashLogin(RedirectView):
    def login_user_or_404(self, signed_pk):
        signer = TimestampSigner(salt=LOGIN_SALT)
        user_pk = signer.unsign(signed_pk, max_age=datetime.timedelta(hours=2))
        user = User.objects.filter(pk=user_pk).first()
        if not user:
            raise Http404
        profile = user.profile
        profile.force_password_change = True
        profile.save()
        login(self.request, user)

    def get(self, *args, **kwargs):
        self.login_user_or_404(kwargs["signed_pk"])
        return super().get(args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse("change-password")

"""
Views for the passwordreset Opal Plugin
"""
from django.urls import reverse_lazy
from django.contrib.auth import views
from . import forms


class PasswordResetView(views.PasswordResetView):
    form_class = forms.OpalPasswordResetForm
    html_email_template_name = "registration/password_reset_email.html"
    email_template_name = 'registration/password_reset_email.txt'


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    """
    A redirect view that if the sign is correct,
    changes the user to force_password_change=True
    and redirects the user to the change password screen.
    """
    post_reset_login = True
    success_url = '/'
    form_class = forms.OpalSetPasswordForm

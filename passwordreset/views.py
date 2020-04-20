"""
Views for the passwordreset Opal Plugin
"""
from django.urls import reverse_lazy
from django.contrib.auth import views
from . import forms


class PasswordResetView(views.PasswordResetView):
    form_class = forms.OpalPasswordResetForm


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    """
    A redirect view that if the sign is correct,
    changes the user to force_password_change=True
    and redirects the user to the change password screen.
    """
    post_reset_login = True
    success_url = reverse_lazy('change-password')

    def get_user(self, *args, **kwargs):
        user = super().get_user(*args, **kwargs)
        profile = user.profile
        profile.force_password_change = True
        profile.save()
        return user

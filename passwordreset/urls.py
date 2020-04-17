"""
Urls for the passwordreset Opal plugin
"""
from django.urls import path

from passwordreset import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
        "passwordreset/request-reset/",
        views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "passwordreset/check-email/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "passwordreset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]

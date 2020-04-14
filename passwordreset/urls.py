"""
Urls for the passwordreset Opal plugin
"""
from django.urls import path

from passwordreset import views

urlpatterns = [
    path("passwordreset/reset_email/", views.RequestReset.as_view(), name="request-reset"),
    path("passwordreset/check/", views.CheckYourEmailPage.as_view(), name="check-email"),
    path("passwordreset/reset/<signed_pk>/", views.HashLogin.as_view(), name="hash-login"),
]

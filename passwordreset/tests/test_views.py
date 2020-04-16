from django.contrib.auth import get_user_model
from unittest import mock
from django.urls import reverse
from opal.core.test import OpalTestCase


class RequestResetTestCase(OpalTestCase):
    def setUp(self):
        User = get_user_model()
        self.post_user = User.objects.create(username="something")
        self.url = reverse("request-reset")

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["passwordreset/send_email_link.html"])

    @mock.patch("passwordreset.views.send_mail")
    def test_post_with_email(self, send_mail):
        self.post_user.email = "something@something.com"
        self.post_user.save()
        response = self.client.post(self.url, {"username": "something"})
        self.assertRedirects(
            response,
            expected_url=reverse("check-email"),
            status_code=302,
            target_status_code=200,
        )
        call_args = send_mail.call_args
        self.assertEqual(call_args[0][3], ["something@something.com"])

    def test_post_with_empty_username(self):
        response = self.client.post(self.url, {"username": "something"})
        self.assertEqual(
            response.context["form"].errors["username"],
            ["Unable to reset your password, please contact your administrator"],
        )

    def test_post_with_user_without_email(self):
        response = self.client.post(self.url, {"username": ""})
        self.assertEqual(
            response.context["form"].errors["username"], ["This field is required."]
        )

    def test_post_with_user_with_fake_username(self):
        response = self.client.post(self.url, {"username": "does not exist"})
        self.assertEqual(
            response.context["form"].errors["username"], ["Unknown username"]
        )

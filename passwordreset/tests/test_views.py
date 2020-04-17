from django.urls import reverse
from opal.core.test import OpalTestCase


class PasswordResetView(OpalTestCase):
    def setUp(self):
        self.url = reverse("password_reset")

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["registration/password_reset_form.html"])


class PasswordChangeDoneViewTestCase(OpalTestCase):
    def setUp(self):
        self.url = reverse("password_reset_done")

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["registration/password_reset_done.html"])
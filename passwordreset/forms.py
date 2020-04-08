from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class SendEmailForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={"autofocus": True, "class": "form-control", "size": 50}
        )
    )

    def clean_username(self):
        username = self.cleaned_data["username"]
        User = get_user_model()
        user = User.objects.filter(
            username=username
        ).first()
        if not user:
            raise ValidationError('Unknown username')

        if not user.email:
            raise ValidationError('Unable to reset your password, please contact your administrator')
        return username


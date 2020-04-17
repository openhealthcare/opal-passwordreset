This is passwordreset - an [Opal](https://github.com/openhealthcare/opal) plugin.

This plugin deals with allowing the user to reset their password.

**This must appear above `django.contrib.admin` in order to use the corrrect templates**


It uses the default password reset views in `django.contrib.auth`.

It changes them in 2 ways..

1. It adds bootstrap styling to the widgets.
2. When we the user has changed their password we automatically
   log them in and redirct them to the change password page.

### Templates
`registration/password_reset_form.html` is the form the user enters their email and receives a reset link.

`registration/password_reset_done.html` is the page that we redirect to after they've entered their email into the above form.


`registration/password_reset_subject.txt` is the email subject line sent to the user.

`registration/password_reset_email.html` is the html email body sent to the user.

`registration/password_reset_confirm.html` is the page they get redirected to after they click on message in their email.

### Views
`PasswordResetView`, is an extended version of the `auth.views.PasswordResetView`. The form view asking the user to enter their email. This just changes the form in the view have bootstrap styling.

`PasswordResetConfirmView` This is the view the user goes to after they have clicked in the link in their email. It
changes `profile.force_password_change` to True, logs them in and redirects them to the password change view.
This is passwordreset - an [Opal](https://github.com/openhealthcare/opal) plugin.

This plugin deals with allowing the user to reset their password.


### Setup

* Add this repo to your requirements.txt.
* Add `passwordreset` to your INSTALLED_APPS in settings.py
* Change your login page to add a reset password link to `request-reset`



## Architecture

The plugin adds three views.


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


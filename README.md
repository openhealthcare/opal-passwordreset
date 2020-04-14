This is passwordreset - an [Opal](https://github.com/openhealthcare/opal) plugin.

This plugin adds views and functionality to allow users to reset their passwords.

It adds three views.

#### request-reset
That asks the user to enter their username and will send an email to the email address related to that user.

It uses the template `passwordreset/send_email_link.html`

#### check-email
A confirmation page that the email has been sent.

It uses the template `passwordreset/check.html`


#### hash-login
A redirect view that redirects the user to the built in opal change password view.



It also uses the template `passwordreset/reset_email.html` as the template for the html email that is sends.


### Setup
Add this repo to your requirements.txt.
Add `passwordreset` to your INSTALLED_APPS in settings.py
Change your login page to add a reset password link to `request-reset`



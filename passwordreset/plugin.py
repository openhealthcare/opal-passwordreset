"""
Plugin definition for the passwordreset Opal plugin
"""
from opal.core import plugins

from passwordreset.urls import urlpatterns

class PasswordresetPlugin(plugins.OpalPlugin):
    """
    Main entrypoint to expose this plugin to our Opal application.
    """
    urls = urlpatterns
    javascripts = {
        # Add your javascripts here!
        'opal.passwordreset': [
            # 'js/passwordreset/app.js',
            # 'js/passwordreset/controllers/larry.js',
            # 'js/passwordreset/services/larry.js',
        ]
    }

    def list_schemas(self):
        """
        Return any patient list schemas that our plugin may define.
        """
        return {}

    def roles(self, user):
        """
        Given a (Django) USER object, return any extra roles defined
        by our plugin.
        """
        return {}
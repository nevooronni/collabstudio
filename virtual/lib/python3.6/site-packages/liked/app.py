from django.apps import AppConfig
from django.conf import settings


class LikedAppConfig(AppConfig):

    name = "liked"

    def ready(self):

        ## Add django activity stream support, if installed.
        if "actstream" in settings.INSTALLED_APPS:
            from actstream import registry
            registry.register(self.get_model("Like"))

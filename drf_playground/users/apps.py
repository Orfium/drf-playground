from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "drf_playground.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import drf_playground.users.signals  # noqa F401 # pylint: disable=unused-import
        except ImportError:
            pass

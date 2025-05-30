from django.apps import AppConfig


class BackendConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.backend"

    def ready(self):
        import apps.backend.signals  # noqa: F401

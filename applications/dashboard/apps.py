from django.apps import AppConfig


class DashboardConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.dashboard"

    def ready(self) -> None:
        from .apis import signals

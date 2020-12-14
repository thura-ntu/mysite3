from django.apps import AppConfig


class NuomiphpConfig(AppConfig):
    name = 'nuomiphp'

    def ready(self):
        from . import signals
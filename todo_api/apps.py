from django.apps import AppConfig


class TodoApiConfig(AppConfig):
    name = 'todo_api'

    def ready(self):
        from .settings import api_settings

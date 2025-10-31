from django.apps import AppConfig



class MakpostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'makpost'

    def ready(self):
        import makpost.signals
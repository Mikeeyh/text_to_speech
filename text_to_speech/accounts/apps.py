from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'text_to_speech.accounts'

    def ready(self):  # Importing signals manually because it is not build-in, it will not create a profile of the user
        import text_to_speech.accounts.signals
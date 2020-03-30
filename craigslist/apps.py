from django.apps import AppConfig


class CraigslistConfig(AppConfig):
    name = 'craigslist'

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import craigslist.signals

from django.conf import settings as django_settings


class Settings(object):
    @property
    def AUTH_USER_MODEL(self):
        return getattr(django_settings, 'AUTH_USER_MODEL', django_settings.AUTH_USER_MODEL)

settings = Settings()


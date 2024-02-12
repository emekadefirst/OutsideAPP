from .base import *
import dj_database_url


ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get("SECRET_KEY_PRODUCTION")

DATABASES = {
    'default': dj_database_url.config(
        default = os.environ.get("DEFAULT")
    )
}

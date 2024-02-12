from .base import *

SECRET_KEY = os.environ.get("SECRET_KEY_LOCAL")

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

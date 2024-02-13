from .base import *
import dj_database_url

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get("SECRET_KEY_PRODUCTION")

import dj_database_url

# Database Configuration
DATABASES = {
    'default': {
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
WHITENOISE_MANIFEST_PREFIX = 'staticfiles/'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

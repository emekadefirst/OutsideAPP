from .base import *
import dj_database_url

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get("SECRET_KEY_PRODUCTION")

import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Corrected typo here
        'NAME': os.environ.get("NAME"),      # Database name
        'USER': os.environ.get("USER"),      # Database user
        'PASSWORD': os.environ.get("PASSWORD"),  # Database password
        'HOST': os.environ.get("HOST"),      # Database host
        'PORT': os.environ.get("PORT"),      # Database port (leave empty for default)
    }
}




# Update the default settings with the parsed database settings


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    # Add paths to additional static file directories here
    # 'C:\\Users\\VICTOR\\Desktop\\serverapp\\server\\server\\static',
]

WHITENOISE_MANIFEST_PREFIX = 'staticfiles/'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

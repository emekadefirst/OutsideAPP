from .base import *
import dj_database_url

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get("SECRET_KEY_PRODUCTION")

import dj_database_url

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'outside_server',  # Database name
        'USER': 'outside_server_user',  # Username
        'PASSWORD': 'IqUHW8eBRUMpE4nX1wXrLF6f02xeS8Lu',  # Password
        'HOST': 'dpg-cn51knfsc6pc73e88od0-a.oregon-postgres.render.com',  # Hostname
        'PORT': '5432',  # Port
    }
}

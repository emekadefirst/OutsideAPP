#Generate secret keys

#Run
"./manage.py shell" or "python manage.py shell"
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

{
  "username": "test_user",
  "password": "test_password",
  "email": "test@example.com"
}

./manage.py makemigrations api --empty
Migrations for 'api':
  api\migrations\0001_initial.py
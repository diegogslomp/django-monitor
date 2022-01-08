#!/bin/sh
# python manage.py collectstatic --noinput
python manage.py migrate
python manage.py loaddata initial_data
python manage.py createsuperuser
#echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

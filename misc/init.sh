#!/bin/sh
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py loaddata initial_data
python manage.py createsuperuser

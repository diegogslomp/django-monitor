#!/bin/sh

while true; do
    until nc -z -v -w5 db 5432
        do
        echo "Waiting 5 seconds for database connection..."
        # wait for 5 seconds before check again
        sleep 5
    done
    python manage.py migrate
    # python manage.py collectstatic --no-input
    # python manage.py loaddata initial_data
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
    gunicorn -b 0.0.0.0:8000 main.wsgi
    sleep 5
done
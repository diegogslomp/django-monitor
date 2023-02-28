#!/bin/sh
# Stop if any error
set -eu

cd /usr/local
python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input
# Create admin user if not created yet
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell || true

# Start web server
gunicorn -b 0.0.0.0:8000 main.wsgi &
# Start monitor daemon
python manage.py monitord &

# Exit if one of the jobs ends
wait -n
exit $?
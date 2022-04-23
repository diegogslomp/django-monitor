#!/bin/sh
# Stop if any error
set -ueo pipefail

# Migrate db
mkdir db || true
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
# Create admin user if not created yet
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell || true
# Add example data
python manage.py loaddata initial_data

# Start web server
gunicorn -b 0.0.0.0:8000 main.wsgi
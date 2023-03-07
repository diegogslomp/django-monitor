#!/bin/sh
# Stop if any error
set -euo pipefail

cd /usr/src/app
python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input

# Start web server
gunicorn -b 0.0.0.0:8000 main.wsgi &
# Start monitor daemon
python manage.py monitord &

# Exit if one of the jobs ends
wait -n
exit $?
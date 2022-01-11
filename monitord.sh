#!/bin/sh

while true; do
    python manage.py monitord || true
    echo "Can't run monitord, waiting 5 seconds..."
    # wait for 5 seconds before check again
    sleep 5
done
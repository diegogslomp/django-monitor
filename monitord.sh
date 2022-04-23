#!/bin/sh
# Stop if any error
set -euo pipefail

# Start monitor daemon
python manage.py monitord
Django Monitor
==============

[![gh-actions](https://github.com/diegogslomp/django-monitor/actions/workflows/docker-image.yml/badge.svg)](https://github.com/diegogslomp/django-monitor/actions)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/diegogslomp/django-monitor/blob/master/LICENSE)

Ping devices and check port status from routers/switches through telnet
connection. Telnet tested on Enterasys S8, G3 and A4 switch series.
<p align="center">
<img src="https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docs/_screenshots/hostlist.png" style="max-height: 440px;"/>
</p>

1. Run local deployment:
  ```
  git clone --single-branch --recurse-submodules https://github.com/diegogslomp/django-monitor.git
  cd django-monitor

  # Create and activate a virtual environment (optional)
  python -m pipenv install --three -r requirements
  python -m pipenv shell

  # Copy/Edit environment variables file
  cp .env.example .env

  # Install dependencies
  pip install -r requirements
  python manage.py createsuperuser
  python manage.py makemigrations
  python manage.py migrate --no-input
  python manage.py collectstatic --no-input

  # Populate DB (optional)
  python manage.py loaddata initial_data

  # Start web app
  python manage.py runserver 0.0.0.0:8000

  # Start monitord in another terminal
  python manage.py monitord
  ```

2. Or run as docker image:
  ```
  docker run -d --restart=unless-stopped \
    -e SECRET_KEY='change_this!o)=4*s#n' \
    -e TIME_ZONE='America/Sao_Paulo' \
    -v $(pwd)/db.sqlite3:/usr/src/app/db.sqlite3 \
    -p 8000:8000 \
    --name monitor diegogslomp/django-monitor

  # Populate DB (optional)
  docker exec monitor python manage.py loaddata initial_data
  ```

1.  Visit <http://localhost:8000>

2.  Visit <http://localhost:8000/admin> to create hosts

3.  To send telegram [bot](https://core.telegram.org/bots) messages, add `TELEGRAM_CHAT_ID` and `TELEGRAM_TOKEN`
    to the docker run command

4.  For PostgreSQL as DB, clone, build and run:
  ```
  git clone --single-branch --recurse-submodules https://github.com/diegogslomp/django-monitor.git
  cd django-monitor
  docker compose build
  docker compose up -d
  ```

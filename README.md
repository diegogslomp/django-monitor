Django Monitor
==============

[![gh-actions](https://github.com/diegogslomp/django-monitor/actions/workflows/docker-image.yml/badge.svg)](https://github.com/diegogslomp/django-monitor/actions)
[![license](https://img.shields.io/github/license/diegogslomp/django-monitor)](https://github.com/diegogslomp/django-monitor/blob/master/LICENSE)
[![gitHub release (latest by date)](https://img.shields.io/github/v/release/diegogslomp/django-monitor)](https://github.com/diegogslomp/django-monitor/releases)

Ping devices and check port status from routers/switches through telnet
connection. Telnet tested on Enterasys S8, G3 and A4 switch series.
<p align="center">
<img src="https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docs/_screenshots/hostlist.png" style="max-height: 440px;"/>
</p>

1. Run docker image:
  ```
  docker run -d --restart=unless-stopped \
    -e SECRET_KEY='change_this!o)=4*s#n' \
    -e TIME_ZONE='America/Sao_Paulo' \
    -v monitor:/usr/src/app \
    -p 8000:8000 \
    --name monitor diegogslomp/django-monitor

  # Create superuser to access admin dashboard
  docker exec -it monitor python manage.py createsuperuser

  # Populate DB (optional)
  docker exec monitor python manage.py loaddata initial_data
  ```

2.  Visit <http://localhost:8000>

3.  Visit <http://localhost:8000/admin> to create hosts

4.  To send telegram [bot](https://core.telegram.org/bots) messages, add `TELEGRAM_CHAT_ID` and `TELEGRAM_TOKEN`
    to the docker run command

5.  For PostgreSQL as DB, clone, build and run:
  ```
  git clone --single-branch --recurse-submodules https://github.com/diegogslomp/django-monitor.git
  cd django-monitor
  docker compose build --pull
  docker compose up -d && docker compose logs -f
  docker compose exec -it monitor python manage.py createsuperuser
  ```

6.  Local deployment:
  ```
  git clone --single-branch --recurse-submodules https://github.com/diegogslomp/django-monitor.git
  cd django-monitor

  # Copy/Edit environment variables file
  cp .env.example .env

  # Create and activate a virtual environment (optional)
  python -m pipenv install
  python -m pipenv shell

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

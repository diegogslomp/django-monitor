Django Monitor
==============

[![gh-actions](https://github.com/diegogslomp/django-monitor/actions/workflows/docker-image.yml/badge.svg)](https://github.com/diegogslomp/django-monitor/actions)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/diegogslomp/django-monitor/blob/master/LICENSE)

Ping devices and check port status from routers/switches through telnet
connection. Telnet tested on Enterasys S8, G3 and A4 switch series.
<p align="center">
<img src="https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docs/_screenshots/hostlist.png" height=220 style="max-height: 440px;"/>
</p>

1.  Run docker image:

        docker run -d --restart=unless-stopped \
          -e SECRET_KEY='change_this!o)=4*s#n' \
          -e TIME_ZONE='America/Sao_Paulo' \
          -v monitordb:/usr/src/app/db \
          -p 8000:8000 \
          --name monitor diegogslomp/django-monitor

2.  Add sample hosts (optional):

        docker exec monitor python manage.py loaddata initial_data

3.  Visit <http://localhost:8000>

4.  Visit <http://localhost:8000/admin> to create hosts (user:admin
    pass:admin)

5.  To send telegram [bot](https://core.telegram.org/bots) messages, add `TELEGRAM_CHAT_ID` and `TELEGRAM_TOKEN`
    to the docker run command

6.  For PostgreSQL as db, clone, build and run:

    git clone --single-branch --recurse-submodules https://github.com/diegogslomp/django-monitor.git
    cd django-monitor
    docker compose build
    docker compose up -d

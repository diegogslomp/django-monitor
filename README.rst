==============
Django Monitor
==============

|gitter| |readthedocs|

A Django application to ping devices and check port status from routers/switches through telnet connection. Tested on Enterasys S8, G3, A4 series.

.. image:: https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docs/_screenshots/webview.gif
    :alt: Index and Detail Pages
    :align: center

Install
-------

#. From dockerhub::

    docker run -d --name monitor -p 8000:8000 diegogslomp/django-monitor
    docker exec -it monitor python manage.py migrate
    docker exec -it monitor python manage.py createsuperuser
    docker exec -d monitor python manage.py monitord

#. Or local nginx + gunicorn + postgres stack::

    git clone --recurse-submodules --depth=1 https://github.com/diegogslomp/django-monitor.git
    cd django-monitor
    cp env.example .env

    docker stack deploy monitor -c stack.yml
    docker exec -it monitor_app.1.xxxx python manage.py migrate
    docker exec -it monitor_app.1,xxxx python manage.py createsuperuser
    docker exec -it monitor_app.1.xxxx python manage.py collectstatic

#. Visit http://localhost:8000/admin to create hosts and ports

#. Visit http://localhost:8000

.. |gitter| image:: https://badges.gitter.im/Join%20Chat.svg
             :alt: Join the chat at https://gitter.im/diegogslomp/django-monitor
             :target: https://gitter.im/diegogslomp/django-monitor?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. |readthedocs| image:: https://readthedocs.org/projects/django-monitor-d/badge/?version=latest
                  :target: http://django-monitor-d.readthedocs.io/en/latest/?badge=latest


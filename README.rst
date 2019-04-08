==============
Django Monitor
==============

|travis| |readthedocs| |gitter|

A Django application to ping devices and check port status from routers/switches through telnet connection. Tested on Enterasys S8, G3, A4 series.

.. image:: https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docs/_screenshots/hostlist.png
    :alt: Host List Page
    :align: center

.. image:: https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docs/_screenshots/hostlog.png
    :alt: Host Log Page
    :align: center

Install
-------

#. Development version::

    git clone --recurse-submodules https://github.com/diegogslomp/django-monitor
    cd django-monitor
    docker-compose up
    docker-compose exec app python manage.py collectstatic
    docker-compose exec app python manage.py migrate
    docker-compose exec app python manage.py loaddata initial_data
    docker-compose exec app python manage.py createsuperuser

#. Or production nginx + gunicorn + postgres stack::

    curl -L https://git.io/fjtgw -o stack.yml
    curl -L https://git.io/fjtgw -o .env
    # Change .env vars
    docker stack deploy monitor -c stack.yml
    docker exec -it monitor_app.1.xxxx python manage.py collectstatic
    docker exec -it monitor_app.1.xxxx python manage.py migrate
    docker exec -it monitor_app.1.xxxx python manage.py createsuperuser

#. Visit http://localhost:8000/admin to create hosts and ports

#. Visit http://localhost:8000

.. |gitter| image:: https://badges.gitter.im/Join%20Chat.svg
             :alt: Join the chat at https://gitter.im/diegogslomp/django-monitor
             :target: https://gitter.im/diegogslomp/django-monitor?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. |readthedocs| image:: https://readthedocs.org/projects/django-monitor-d/badge/?version=latest
                  :target: http://django-monitor-d.readthedocs.io/en/latest/?badge=latest
                  
.. |travis| image:: https://travis-ci.org/diegogslomp/django-monitor.svg?branch=master
             :target: https://travis-ci.org/diegogslomp/django-monitor                  


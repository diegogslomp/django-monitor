==============
Django Monitor
==============

|license| |travis| |readthedocs| |gitter|

A Django application to ping devices and check port status from routers/switches through telnet connection. Tested on Enterasys S8, G3, A4 series.

.. image:: https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docs/_screenshots/hostlist.png
    :alt: Host List Page
    :align: center

Prerequisites
-------------

    Docker_ and docker-compose_ if building the stack

Install
-------

#. Clone this repo::

    git clone --depth=1 -j8 --recurse-submodules git://github.com/diegogslomp/django-monitor
    cd django-monitor

#. Create and edit .env file variables::

    mv env-example .env

#. Run a nginx + django + postgres stack::

    # Build stack services
    docker-compose up --build

    # Open another terminal and collect static files, migrate and create superuser
    docker-compose run app ./init.sh

#. Or build a single container with django + sqlite::

    # Build image
    docker build -t monitor:latest .

    # Run gunicorn server
    docker run -d -p 8000:8000 --name monitor monitor:latest

    # Collect static files, migrate and create superuser
    docker exec -it monitor ./init.sh

    # Run monitord agent
    docker exec -d monitor python manage.py monitord

#. Visit http://localhost:8000/admin to create hosts

#. Visit http://localhost:8000

.. _Docker: https://www.docker.com

.. _docker-compose: https://docs.docker.com/compose/install

.. |gitter| image:: https://badges.gitter.im/Join%20Chat.svg
             :alt: Join the chat at https://gitter.im/diegogslomp/django-monitor
             :target: https://gitter.im/diegogslomp/django-monitor?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. |readthedocs| image:: https://readthedocs.org/projects/django-monitor-d/badge/?version=latest
                  :target: http://django-monitor-d.readthedocs.io/en/latest/?badge=latest
                  
.. |travis| image:: https://travis-ci.org/diegogslomp/django-monitor.svg?branch=master
             :target: https://travis-ci.org/diegogslomp/django-monitor                  

.. |heroku| image:: https://heroku-badge.herokuapp.com/?app=heroku-badge&style=flat&svg=1
             :target: https://django-monitor.herokuapp.com

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
             :target: https://github.com/diegogslomp/django-monitor/blob/master/LICENSE

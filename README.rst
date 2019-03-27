==============
Django Monitor
==============

|gitter| |readthedocs|

A `Django <https://www.djangoproject.com>`_ application to ping devices and check port status from routers/switches through telnet connection. Tested on Enterasys S8, G3, A4 series.

.. image:: https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docs/_screenshots/webview.gif
    :alt: Index and Detail Pages
    :align: center

Docker
------

#. Install `docker <https://docker.com>`_ and `docker-compose <https://docs.docker.com/compose>`_::

    git clone --recurse-submodules --depth=1 https://github.com/diegogslomp/django-monitor.git
    cd django-monitor
    docker-compose up
    docker exec -it monitor python manage.py createsuperuser

#. Visit http://localhost:8000/admin to create hosts and ports

#. Visit http://localhost:8000

Local
-----

#. Python3 linux system::

    git clone --recurse-submodules --depth=1 https://github.com/diegogslomp/django-monitor.git
    cd django-monitor
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver 0.0.0.0:8000


#. Visit http://localhost:8000/admin to create hosts and ports

#. Start another terminal and run the host monitor daemon::

    python manage.py monitord

#. Visit http://localhost:8000

.. |gitter| image:: https://badges.gitter.im/Join%20Chat.svg
             :alt: Join the chat at https://gitter.im/diegogslomp/django-monitor
             :target: https://gitter.im/diegogslomp/django-monitor?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. |readthedocs| image:: https://readthedocs.org/projects/django-monitor-d/badge/?version=latest
                  :target: http://django-monitor-d.readthedocs.io/en/latest/?badge=latest

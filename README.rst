==============
Django Monitor
==============

|gitter| |readthedocs|

A `Django <https://www.djangoproject.com>`_ application to ping devices and check port status from routers/switches through telnet connection. Tested on Enterasys S8, G3, A4 series.

.. image:: https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docs/_screenshots/webview.gif
    :alt: Index and Detail Pages
    :align: center

How-To
------

#. Clone, install using `pipenv <https://pipenv.readthedocs.io>`_, migrate, create admin and run it::

    git clone --recurse-submodules https://github.com/diegogslomp/django-monitor.git
    cd django-monitor
    pipenv install --three
    pipenv run python manage.py migrate
    pipenv run python manage.py createsuperuser
    pipenv run python manage.py runserver 0.0.0.0:8000

#. Visit http://localhost:8000/admin to create hosts and services.

#. Start another terminal and run the host monitor daemon::

    pipenv run python manage.py monitord

#. Visit http://localhost:8000

.. |gitter| image:: https://badges.gitter.im/Join%20Chat.svg
             :alt: Join the chat at https://gitter.im/diegogslomp/django-monitor
             :target: https://gitter.im/diegogslomp/django-monitor?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. |readthedocs| image:: https://readthedocs.org/projects/django-monitor-d/badge/?version=latest
                  :target: http://django-monitor-d.readthedocs.io/en/latest/?badge=latest

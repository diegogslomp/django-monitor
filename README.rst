=======
Monitor
=======

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/diegogslomp/django-monitor
   :target: https://gitter.im/diegogslomp/django-monitor?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

Monitor is a `Django <https://www.djangoproject.com>`_ app to monitor hosts. Also checks port status for registered ports using telnet connection. Tested on routers/switches Enterasys S8, G3 and A4 series.

.. image:: https://raw.githubusercontent.com/diegogslomp/django-monitor/master/images/webview.gif
    :alt: Index and Detail Pages
    :align: center

How-To
------

#. Create a django project and clone the app::

    pip install django
    django-admin.py startproject mysite
    cd mysite
    git clone https://github.com/diegogslomp/monitor.git

#. Add "monitor" to INSTALLED_APPS in mysite/settings.py::

    ALLOWED_HOSTS = ['*']

    INSTALLED_APPS = (
        ...
        'monitor',
    )

#. Include the monitor URLconf in mysite/urls.py::

    from django.urls import include, path

    urlpatterns = [
        ...
        path('monitor/', include('monitor.urls')),
    ]

#. Migrate, create superuser and start the server::

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver 0.0.0.0:8000

#. Visit http://localhost:8000/admin to create hosts and services (need the Admin app enabled).

#. Start another terminal and run the monitor daemon to start monitoring::

      python manage.py monitord

#. Visit http://localhost:8000/monitor

Logging
-------

#. Add to mysite/settings.py::

      ...
      LOGGING = {
          "version": 1,
          "disable_existing_loggers": False,
          "formatters":{
              "console": {
                  "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
              }
          },
          "handlers": {
              "console": {
                  "class": "logging.StreamHandler",
                  "formatter": "console",
              },
          },
          "loggers": {
              "": {
                  "handlers": ["console"],
                  "level": "DEBUG",
              },
          },
      }

#. Run ``python manage.py monitord`` from command-line

=======
Monitor
=======

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/diegogslomp/django-monitor
   :target: https://gitter.im/diegogslomp/django-monitor?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

Monitor is a `Django <https://www.djangoproject.com>`_ app to monitor hosts. Also checks port status for registered ports using telnet connection. Tested on routers/switches Enterasys S8, G3 and A4 series.

.. image:: https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docs/host_list_example.png
    :alt: Monitor Index Page
    :align: center

.. image:: https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docs/host_log_example.png
    :alt: Monitor Detail Page
    :align: center
      
How-To
-------

1. Create a django project and clone the app::

    pip install django paramiko nltk
    django-admin.py startproject mysite
    cd mysite
    git clone https://github.com/diegogslomp/monitor.git  

2. Add "monitor" to INSTALLED_APPS in mysite/settings.py::

    ALLOWED_HOSTS = ['*']

    INSTALLED_APPS = (
        ...
        'monitor',
    )
    
3. Include the monitor URLconf in mysite/urls.py::
    from django.conf.urls import url, include

    url(r'^monitor/', include('monitor.urls', namespace='monitor')),

4. Migrate, create superuser and start the server::

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver 0.0.0.0:8000
    
5. Visit http://localhost:8000/admin to create hosts and services (need the Admin app enabled).

6. Run the monitor daemon to start monitoring::

      python manage.py monitord

7. Visit http://localhost:8000/monitor


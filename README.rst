=======
Monitor
=======

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/chonpz28/django-monitor
   :target: https://gitter.im/chonpz28/django-monitor?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

Monitor is a simple Web-based `Django <https://www.djangoproject.com>`_ app to monitor hosts through ICMP packets (ping) using `this daemon <https://github.com/chonpz28/django-monitor/blob/master/monitor/management/commands/monitord.py>`_.

.. image:: https://raw.githubusercontent.com/chonpz28/django-monitor/master/docs/host_list_example.png
    :alt: Monitor Index Page
    :width: 730
    :height: 290
    :align: center
      
How-To
-------

1. It's recommended to use `pyenv <https://github.com/yyuu/pyenv>`_ for Python install. See this `script <https://github.com/chonpz28/django-monitor/blob/master/docs/centos_install.sh>`_ to install it on Centos or `this <https://github.com/chonpz28/django-monitor/blob/master/docs/ubuntu_install.sh>`_ to install it on Ubuntu/Debian. 
 

2. Create a project::

    django-admin.py startproject foo_project
    
3. Download and Install app from github::

    pip install https://github.com/chonpz28/django-monitor/raw/master/dist/django-monitor-0.1.6.tar.gz

4. Add "monitor" to project's setting INSTALLED_APPS (/foo_project/foo_project/settings.py)::

    INSTALLED_APPS = (
        ...
        'monitor',
    )
    
5. Include the monitor URLconf in your project urls.py::

    url(r'^monitor/', include('monitor.urls', namespace='monitor')),

6. Migrate hosts models to project's database::

    python manage.py migrate

7. Create superuser if a new project was created::

    python manage.py createsuperuser
    
8. Start the development server::
   
    python manage.py runserver 0.0.0.0:8000
    
9. Visit http://localhost:8000/admin/ to create hosts and services (need the Admin app enabled).

10. Run the monitor daemon to start monitoring::

      python manage.py monitord

11. Visit http://localhost:8000/monitor/

12. Enjoy!



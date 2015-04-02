=======
Monitor
=======

Monitor is a simple Web-based Django app to monitor linux hosts through ICMP packets (ping). Also, supports custom shell commands to verify host service states through SSH. The returned code will change the host status.


How-To
-------

1. It's recomended to use `pyenv <https://github.com/yyuu/pyenv>`_ for Python >= 2.7.6 install.
   
2. For Centos 6.6 without pyenv, see this `script <https://github.com/chonpz28/django-monitor/blob/master/docs/centos6.6_install.sh>`_. More details in this `blog <http://bicofino.io/blog/2014/01/16/installing-python-2-dot-7-6-on-centos-6-dot-5>`_. 

3. Create a project::

    django-admin.py startproject mysite
    
4. Download and Install app from github::

    pip install https://github.com/chonpz28/django-monitor/raw/master/dist/django-monitor-0.1.tar.gz

5. Add "monitor" to your INSTALLED_APPS setting::

    INSTALLED_APPS = (
        ...
        'monitor',
    )
    
6. Include the monitor URLconf in your project urls.py::

    url(r'^monitor/', include('monitor.urls')),

7. Migrate hosts models to project's database::

    python manage.py migrate

8. Create superuser if not created yet::

    python manage.py createsuperuser
    
9. Start the development server and visit http://localhost:8000/admin/ to create a host (need the Admin app enabled)::
   
    python manage.py runserver 0.0.0.0:8000

10. Visit http://localhost:8000/monitor/ to see the host list.

11. Add hosts, run the monitor daemon and input SSH credentials to start monitoring::

        python manage.py monitord
        
12. Enjoy!
    

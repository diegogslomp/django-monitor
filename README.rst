==============
Django Monitor
==============

|license| |travis| |readthedocs| |gitter|

A Django application to ping devices and check port status from routers/switches through telnet connection. Telnet tested on Enterasys S8, G3 and A4 switch series.

.. image:: https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docs/_screenshots/hostlist.png
    :alt: Host List Page
    :align: center

#. Download docker-compose.yml file::

    curl -LO https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docker-compose.yml
    
#. Run hosts and show logs (Ctrl+c to exit)::

    docker-compose up -d && docker-compose logs -f

#. Visit http://localhost:8000/admin to create hosts (user:admin pass:admin), for sample data run::

    docker-compose exec app python manage.py loaddata initial_data

#. Visit http://localhost:8000

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

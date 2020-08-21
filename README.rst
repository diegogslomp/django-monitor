==============
Django Monitor
==============

|license| |travis| |readthedocs| |gitter|

A Django application to ping devices and check port status from routers/switches through telnet connection. Tested on Enterasys S8, G3, A4 series.

.. image:: https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docs/_screenshots/hostlist.png
    :alt: Host List Page
    :align: center

#. Copy django + postgres yml file::

    curl -o monitor.yml https://raw.githubusercontent.com/diegogslomp/django-monitor/master/docker-compose.yml
    
#. Run docker swarm and start the stack::

    docker swarm init
    docker stack deploy -c monitor.yml monitor

#. Collect static files, migrate db and create superuser::

    docker exec -it monitor_app.xxxx ./init.sh
    
#. Visit http://localhost:8000/admin to create hosts

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

=======
Monitor
=======

Monitor is a simple Web-based Django app to monitor linux hosts through ICMP packets. Add commands to each services to verify the state through SSH tunel.


Quick start
-----------

1. Add "monitor" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'monitor',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^monitor/', include('monitor.urls')),

3. Run `python manage.py migrate` to create the hosts models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a host (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/monitor/ to see the host list.

6. Start the custom-admin command daemon (python manage.py daemon) to input SSH connection info and start verify each host added in the admin page. 

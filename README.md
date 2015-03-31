=======
Monitor
=======

Monitor is a simple Web-based Django app to monitor linux hosts through ICMP packets. Add commands to each services to verify the state through SSH tunel.


How-To
-------

1. Bellow check how to install [Django](https://www.djangoproject.com) and get django-monitor app working on a fresh Centos 6.6 install. More info [here](http://bicofino.io/blog/2014/01/16/installing-python-2-dot-7-6-on-centos-6-dot-5):

    ```bash
    ifup eth0
    iptables -F
    yum update -y
    yum groupinstall -y 'development tools'
    yum install -y zlib-devel bzip2-devel openssl-devel xz-libs wget sqlite-devel
    wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tar.xz
    xz -d Python-2.7.9.tar.xz
    tar -xvf Python-2.7.9.tar
    cd Python-2.7.9
    ./configure --prefix=/usr/local
    make
    make altinstall
    export PATH="/usr/local/bin:$PATH"
    curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | python2.7 -
    pip2.7 install django setuptools paramiko
    ```
    
2. Create a project::

    ```bash
    cd /opt/
    django-admin.py startproject mysite
    cd mysite/
    ```
    
3. Download and Install app from github::

    `pip2.7 install https://github.com/chonpz28/django-monitor/blob/development/dist/django-monitor-0.1.tar.gz?raw=true`

4. Add "monitor" to your INSTALLED_APPS setting like this::

    ```
    INSTALLED_APPS = (
        ...
        'monitor',
    )
    ```
    
2. Include the polls URLconf in your project urls.py:

    ```
    url(r'^monitor/', include('monitor.urls')),
    ```

3. Run `python manage.py migrate` to create the hosts models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a host (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/monitor/ to see the host list.

6. Add hosts, run `python manage.py daemon` and input SSH credentials to start the services monitoring. 

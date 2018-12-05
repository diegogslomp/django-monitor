FROM python

WORKDIR /usr/src/app

COPY . . 

# RUN apt install git -t \
#    && git clone --recurse-submodules --depth=1 https://github.com/diegogslomp/django-monitor.git . \

RUN pip install virtualenv \
    && mkdir -p ../envs \
    && virtualenv ../envs/monitor -p python3 \
    && ../envs/monitor/bin/pip install -r requirements.txt \
    && ../envs/monitor/bin/python manage.py migrate \
    && virtualenv ../envs/supervisor -p python2 \
    && ../envs/supervisor/bin/pip install supervisor

CMD ["../envs/supervisor/bin/supervisord", "-c", "supervisord.conf"]

EXPOSE 8000

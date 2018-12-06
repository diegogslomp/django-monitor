FROM python

WORKDIR /usr/local/src/app

COPY . . 

ENV DJANGO_LOG_LEVEL='DEBUG'
ENV TELNET_USER='admin'
ENV TELNET_PASS='secret'
ENV DJANGO_SECRET_KEY='super_secret_key'

RUN pip install virtualenv \
    && mkdir -p envs \
    && virtualenv envs/monitor -p python3 \
    && virtualenv envs/supervisor -p python2 \
    && envs/monitor/bin/pip install -r requirements.txt \
    && envs/monitor/bin/python manage.py migrate \
    && envs/monitor/bin/python manage.py collectstatic \
    && envs/supervisor/bin/pip install supervisor

CMD ["envs/supervisor/bin/supervisord", "-c", "supervisord.conf"]

EXPOSE 8000


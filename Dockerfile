FROM python:alpine

WORKDIR /usr/src/app

COPY . . 

RUN apk install git -y \
#    && git clone --recurse-submodules --depth=1 https://github.com/diegogslomp/django-monitor.git . \
    && pip install pipenv \
    && pipenv install --three \
    && pipenv run python manage.py migrate
    && mkdir -p ../envs \
    && virtualenv ../envs/supervisor -p python2 \
    && ../envs/supervisor/bin/pip install supervisor

CMD ["../env/supervisord/bin/supervisord", "-c", "supervisord.conf"]

EXPOSE 8000

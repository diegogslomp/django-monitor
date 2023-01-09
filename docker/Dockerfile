FROM python:alpine

RUN apk add --update --no-cache \
    curl postgresql-dev gcc python3-dev musl-dev

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN django-admin startproject main .

COPY main/settings.py main/settings.py
COPY main/urls.py main/urls.py
COPY monitor monitor

COPY docker/sbin /usr/local/sbin
COPY docker/supervisord.conf /etc/supervisord.conf

CMD supervisord

EXPOSE 8000

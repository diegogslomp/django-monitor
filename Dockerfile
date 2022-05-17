FROM python:alpine

RUN apk add --no-cache curl postgresql-dev gcc python3-dev musl-dev

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN django-admin startproject main .

COPY main/settings.py main/settings.py
COPY main/urls.py main/urls.py
COPY monitor monitor

COPY sbin /usr/local/sbin
COPY supervisord.conf supervisord.conf

CMD supervisord -c supervisord.conf

EXPOSE 8000

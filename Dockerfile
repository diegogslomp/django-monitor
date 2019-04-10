FROM python:alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /usr/src/app

COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

COPY main main
COPY manage.py manage.py
COPY monitor monitor

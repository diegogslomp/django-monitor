FROM python:alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /usr/src/app

COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY main main
COPY manage.py manage.py
COPY monitor monitor
COPY init.sh init.sh

CMD gunicorn -b 0.0.0.0:8000 main.wsgi

EXPOSE 8000

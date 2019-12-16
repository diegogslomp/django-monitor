FROM python:alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /usr/src/app

COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY=secret
ENV DEBUG=False
ENV ALLOWED_HOSTS=*
ENV DB_ENGINE=django.db.backends.postgresql_psycopg2
ENV DB_NAME=postgres
ENV DB_USER=postgres
ENV DB_PASS=postgres
ENV DB_HOST=db
ENV DB_PORT=5432
ENV LANGUAGE_CODE=en-us
ENV LOG_LEVEL=INFO
ENV TIME_ZONE=UTC

COPY main main
COPY manage.py manage.py
COPY monitor monitor
COPY init.sh init.sh

CMD gunicorn -b 0.0.0.0:8000 main.wsgi

EXPOSE 8000

FROM python:3.11-alpine

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
COPY run.sh run.sh
CMD ["/usr/src/app/run.sh"]

EXPOSE 8000

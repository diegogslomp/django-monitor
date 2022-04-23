FROM python:alpine

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

WORKDIR /usr/src/app

COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN django-admin startproject main .
RUN mv main/settings.py main/settings.ORIG.py
RUN mv main/urls.py main/urls.ORIG.py

COPY main/settings.py main/settings.py
COPY main/urls.py main/urls.py

COPY monitor monitor
COPY monitor.sh monitor.sh
COPY monitord.sh monitord.sh
COPY supervisord.conf supervisord.conf

CMD supervisord -c supervisord.conf

EXPOSE 8000

FROM python

ENV DJANGO_SECRET_KEY super_secret_key
ENV DJANGO_LOG_LEVEL DEBUG
ENV TELNET_USER admin
ENV TELNET_PASS secret

WORKDIR /usr/src/app

COPY . . 

RUN apt update \
    && apt install supervisor -y \
    && mv supervisord.conf /etc/supervisord.conf \
    && pip install -r requirements.txt \
    && python manage.py migrate \
    && python manage.py collectstatic

CMD ["supervisord"]

EXPOSE 8000


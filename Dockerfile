FROM python:3-alpine

WORKDIR /usr/src/app
COPY . .

# RUN apk install git -y && \
#     git clone --recurse-submodules --depth=1 https://github.com/diegogslomp/django-monitor.git .

RUN pip install pipenv && \
    pipenv install --three && \
    pipenv run python manage.py migrate
#    pipenv run python manage.py createsuperuser && \

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:80"]
CMD ["pipenv", "run", "python", "manage.py", "monitord"]

EXPOSE 80

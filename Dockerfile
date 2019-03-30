FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /usr/src/app
COPY . . 

RUN pip install -r requirements.txt

RUN python manage.py migrate
RUN python manage.py 
RUN echo "from django.contrib.auth import get_user_model; \
  User = get_user_model(); \
  User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" \
  | python manage.py shell
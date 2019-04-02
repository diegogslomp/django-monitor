FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /usr/src/app

COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY . . 

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

EXPOSE 8000

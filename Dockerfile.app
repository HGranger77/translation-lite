FROM python:3.12-slim

WORKDIR /app

EXPOSE 8501

ADD /requirements/requirements-app.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

ADD /src/app /app

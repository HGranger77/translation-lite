FROM python:3.12-slim

WORKDIR /app

EXPOSE 8501

ADD /requirements/requirements-app.txt /app/requirements-app.txt

RUN pip3 install -r requirements-app.txt

ADD /languages_config.yaml /app/languages_config.yaml
ADD /src/app /app

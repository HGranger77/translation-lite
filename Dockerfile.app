FROM python:3.12-slim

WORKDIR /app

EXPOSE 8501

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

ADD /requirements/requirements-app.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

ADD /src/app /app

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

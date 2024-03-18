FROM python:3.9-slim

RUN mkdir /app
WORKDIR /app
RUN mkdir /app/storage

COPY requirements.txt .
RUN apt-get -y update \
    && apt-get -y install git \
    && apt-get -y install fluidsynth \
    && pip install --no-cache -r requirements.txt

COPY . .
FROM python:3.9-slim

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && apt-get -y install fluidsynth \
    && apt-get -y install libmp3lame-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache -r requirements.txt

EXPOSE 8501

COPY . . -storage/
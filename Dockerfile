# Use the official Python 3.9 slim image
FROM python:3.9-slim-buster

RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD ["bash", "start"]
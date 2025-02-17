FROM ubuntu:22.04

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && \
apt-get install -y pkg-config build-essential python3-pip python3-dev default-libmysqlclient-dev && \
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

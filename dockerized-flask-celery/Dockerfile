FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN <<LAYER
groupadd -g 1000 app
useradd -m -d /app -s /bin/bash -u 1000 -g 1000 app
chown app:app /app
LAYER

RUN <<LAYER
apt-get update
# dependencies for building Python packages
# apt-get install -y build-essential
# cleaning up unused files
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
rm -rf /var/lib/apt/lists/*
LAYER

COPY ./requirements.txt /requirements.txt
RUN <<LAYER
# pip3 install --no-cache-dir --update pip3
pip3 install --no-cache-dir -r /requirements.txt
LAYER

USER app
WORKDIR /app

COPY --chown=1000:1000 . .

RUN <<LAYER
cp .env.docker .env
LAYER

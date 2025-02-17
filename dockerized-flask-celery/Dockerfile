FROM ubuntu:22.04

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && \
apt-get install --no-install-recommends -y \
pkg-config \
build-essential \
libmysqlclient-dev default-libmysqlclient-dev \
python3-dev \
python3-pip && \
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

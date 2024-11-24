FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN <<LAYER
apt-get update
# dependencies for building Python packages
apt-get install -y build-essential 
# cleaning up unused files
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
rm -rf /var/lib/apt/lists/*
LAYER

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

WORKDIR /app
COPY . .

# RUN chmod +x entrypoint.sh
# ENTRYPOINT ["./entrypoint.sh"]

RUN chmod +x runworker.sh
ENTRYPOINT ["./runworker.sh"]


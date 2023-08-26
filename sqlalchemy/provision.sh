#!/bin/bash

# get current
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install -y build-essential python3-dev python3-setuptools python3-pip python3-venv
sudo apt-get install -y sqlite3

[ -d /vagrant ] && cd /vagrant

python3 -m venv venv
venv/bin/pip install -r requirements.txt

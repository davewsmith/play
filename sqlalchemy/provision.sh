#!/bin/bash

# get current
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install -y build-essential python3-dev python3-setuptools python3-pip python3-venv
sudo apt-get install -y sqlite3

cd /vagrant

# N.B. We build the venv in /home/vagrant instead of /vagrant
#  because of an issue with (not) deleting files sync'd folders.
#  See https://github.com/hashicorp/vagrant/issues/12057 and
#  https://www.virtualbox.org/ticket/8761
python3 -m venv /home/vagrant/venv
source /home/vagrant/venv/bin/activate
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt

#!/bin/bash

rm -rf venv.ansible

# Because my scratch laptop is on 14.04
# virtualenv --python=python3 venv.ansible
# venv.ansible/bin/pip install --upgrade pip
virtualenv venv.ansible
venv.ansible/bin/pip install --upgrade pip

venv.ansible/bin/pip install ansible

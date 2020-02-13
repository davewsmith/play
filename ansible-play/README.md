# Ansible Playground

Mucking about with using Ansible to provision a VM

## Requirements

* VirtualBox (`sudo apt-get install virtualbox`)
* Vagrant (from https://vagrantup.com/)

## Setup

The only unusual thing here is putting ansible in a virtual environment to avoid (further) polluting system.

    $ ./setup.sh
    $ . venv.ansible/bin/activate
    $ vagrant up

## References

* https://www.vagrantup.com/docs/provisioning/ansible_intro.html
* https://www.vagrantup.com/docs/provisioning/ansible.html


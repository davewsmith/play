# Ansible Playground

Mucking about with using Ansible to provision a VM

## Requirements

* VirtualBox (`sudo apt-get install virtualbox`)
* Vagrant (from https://vagrantup.com/)

## Setup

    $ ./setup.sh
    $ . venv.ansible/bin/activate
    $ vagrant up
    ...
    $ vagrant destroy -f

## References

* https://www.vagrantup.com/docs/provisioning/ansible_intro.html
* https://www.vagrantup.com/docs/provisioning/ansible.html


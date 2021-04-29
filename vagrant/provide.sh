#!/usr/bin/env bash

sudo yum -y update
sudo yum -y install vim
sudo yum -y install epel-release
sudo yum -y update
sudo yum -y install ansible


## Ansible magic
ansible-playbook /repos/dev-ops-sandbox/ansible/install-tools.yml
ansible-playbook /repos/dev-ops-sandbox/ansible/configure-database.yml

sudo pip3 install --upgrade django

cd /repos/Projekt_studia/projekt/src/baza
python3 manage.py migrate
python3 manage.py runserver 192.168.33.10:8000

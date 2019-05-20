#!/bin/bash

source ssh-monitoring-lib.sh

sudo useradd test_user

sudo -u test_user  mkdir -p /home/test_user/.ssh
sudo -u test_user chmod 0700 /home/test_user/.ssh

sudo -u test_user ssh-keygen -f /home/test_user/.ssh/id_rsa -q -N "" &> /dev/null
sudo -u test_user cp /home/test_user/.ssh/id_rsa.pub /home/test_user/.ssh/authorized_keys

sudo -u test_user ssh -tt -o "StrictHostKeyChecking=no" -i /home/test_user/.ssh/id_rsa 127.0.0.1 "sleep 5" &> /dev/null &
sleep 1

check_ssh

wait 

sudo userdel -fr test_user &> /dev/null

if [[ ! $OUTPUT == *"test"* ]] ; then
	echo "FUUUUUUUUUUUUUUCK"
	exit 1
fi

exit 0


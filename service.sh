#!/bin/bash

TMP="$( netstat -atp | grep 'ESTABLISHED.*sshd' | tr -s ' ' ' ' | cut -d' ' -f8 | grep -v "\[" )";
function check_ssh {
	OUTPUT="$( diff <(echo "$TMP") <(netstat -atp | grep 'ESTABLISHED.*sshd' | tr -s ' ' ' ' | cut -d' ' -f8 | grep -v "\[" ) | grep ">" )";
	[[ ! -z "$OUTPUT" ]] && awk '{ print $0, "logged in via SSH" }' <(echo "$OUTPUT") | wall;
	TMP="$( netstat -atp | grep 'ESTABLISHED.*sshd' | tr -s ' ' ' ' | cut -d' ' -f8 | grep -v "\[" )";
}

trap 'check_ssh' USR1;

while sleep 5; do
	check_ssh
done;

exit 0


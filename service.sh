#!/bin/bash

TMP="$( ps auxwww | grep sshd: | grep @ | tr -s ' ' ' ' | cut -d' ' -f12 | cut -d'@' -f12 )";
function check_ssh { 
	OUTPUT="$( ps auxwww | grep sshd: | grep @ | tr -s ' ' ' ' | cut -d' ' -f12 | cut -d'@' -f12 )";
	[[ ! -z "$OUTPUT" ]] && awk '{ print $0, "logged in via SSH" }' <(echo "$OUTPUT") | wall;
	TMP="$( ps auxwww | grep sshd: | grep @ | tr -s ' ' ' ' | cut -d' ' -f12 | cut -d'@' -f12 )";
}

trap 'check_ssh' USR1;

while sleep 5; do
	check_ssh
done;

exit 0


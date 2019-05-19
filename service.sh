#!/bin/bash

TMP="$( netstat -atp | grep 'ESTABLISHED.*sshd' | tr -s ' ' ' ' | cut -d' ' -f8 | grep -v "\[" )";
function check_ssh {
	OUTPUT="$( diff <(echo "$TMP") <(netstat -atp | grep 'ESTABLISHED.*sshd' | tr -s ' ' ' ' | cut -d' ' -f8 | grep -v "\[" ) | grep ">" )";
	TMP="$( netstat -atp | grep 'ESTABLISHED.*sshd' | tr -s ' ' ' ' | cut -d' ' -f8 | grep -v "\[" )";
}

trap ' check_ssh; [[ ! -z "$OUTPUT" ]] && awk "{ print $0, "logged in via SSH" }" <(echo "$OUTPUT"); logger SIGUSR1 recieved "$OUTPUT" ' USR1;
trap ' logger SSH-monitoring service stopped && exit 0' SIGTERM;

logger SSH-Monitoring service started;

while true; do
	check_ssh
	[[ ! -z "$OUTPUT" ]] && awk '{ print $0, "logged in via SSH" }' <(echo "$OUTPUT") | wall
	[[ ! -z "$OUTPUT" ]] && logger "$OUTPUT"
	sleep 5 &
	wait
done;

exit 0


#!/bin/bash

TMP="$( ps aux | grep ssh | grep @ | tr -s ' ' ' ' | cut -d' ' -f12 | cut -d'@' -f1 )";
function check_ssh {
	OUTPUT="$( diff <(echo "$TMP") <(ps aux | grep ssh | grep @ | grep -v grep | grep -v cut | tr -s ' ' ' ' | cut -d' ' -f12 | cut -d'@' -f1 ) | grep ">" )";
	TMP="$( ps aux | grep ssh | grep @ | tr -s ' ' ' ' | cut -d' ' -f12 | cut -d'@' -f1 )";
}


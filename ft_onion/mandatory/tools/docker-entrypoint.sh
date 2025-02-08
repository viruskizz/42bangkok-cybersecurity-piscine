#!/bin/bash
NO_FORMAT="\033[0m"
YELLOW="\033[33m"

# /usr/sbin/sshd -D -e
tor -f /etc/tor/torrc & \
# Sleep for waiting tor initialize
sleep 20

ONION_SITE=$(cat /var/lib/tor/mandatory/hostname)
echo -e $YELLOW"ONION_SITE=$ONION_SITE"$NO_FORMAT

nginx -g "daemon off;"
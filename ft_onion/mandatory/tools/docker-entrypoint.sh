#!/bin/bash
RESET="\033[0m"
GREEN="\033[32m"
YELLOW="\033[33m"

# Start sshd
/etc/init.d/ssh restart
echo -e $GREEN"SSHD server restart"$RESET

# Start tor and wait initialize
tor -f /etc/tor/torrc &
sleep 30
ONION_SITE=$(cat /var/lib/tor/mandatory/hostname)
echo -e $YELLOW"ONION_SITE=$ONION_SITE"$RESET

# Start nginx
nginx -g "daemon off;"
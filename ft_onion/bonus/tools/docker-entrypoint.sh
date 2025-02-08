#!/bin/bash
TOR_DIR=/var/lib/tor/bonus
RESET="\033[0m"
GREEN="\033[32m"
YELLOW="\033[33m"

#########################################
# Start sshd
/etc/init.d/ssh restart
echo -e $GREEN"SSHD server restart"$RESET

#########################################
# Start tor and wait initialize
tor & sleep 30
ONION_SITE=$(cat $TOR_DIR/hostname)
echo -e $YELLOW"ONION_SITE=$ONION_SITE"$RESET

echo -e $GREEN"Tor network started"$RESET
echo -e $YELLOW"Generating Tor client credential"$NO_FORMAT
/tools/generate-auth.sh
# Restart Tor
echo -e $YELLOW"Restarting Tor network"$NO_FORMAT
ps
kill -9 $(ps | grep tor | awk '{print $1}')
tor & sleep 30
echo -e $GREEN"Tor network restarted"$RESET

ONION_SITE=$(cat $TOR_DIR/hostname)
echo -e $YELLOW"ONION_SITE=$ONION_SITE"$RESET

#########################################
# Start expressjs
node /app/index.js
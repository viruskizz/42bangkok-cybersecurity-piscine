#!/bin/bash
TOR_DIR=/var/lib/tor/bonus
NO_FORMAT="\033[0m"
YELLOW="\033[33m"

# Init tor
tor &
sleep 20

# echo -e $YELLOW"Copy cred to HiddenService"$NO_FORMAT
# cp /tools/cred/viruskizz.auth /var/lib/tor/bonus/authorized_clients

# PRIVATE_KEY=$(/var/lib/tor/bonus/authorized_clients/viruskizz.auth)
ONION_SITE=$(cat /var/lib/tor/bonus/hostname)
# ONION_SITE_NAME=$(echo "$ONION_SITE" | sed 's/.onion//g')
# "$ONION_SITE_NAME':descriptor:x25519:$PUBLIC_KEY


# Restart Tor
# kill -9 $(ps | grep tor | awk '{print $1}')
# tor &
/etc/init.d/ssh start

echo -e $YELLOW"ONION_SITE=$ONION_SITE"$NO_FORMAT
node /app/index.js

# torify ssh root@25tfmlgaq2ujmli3sn3z7usc4uavwwrthmq6zt5a33d7zmfy53ldb3yd.onion
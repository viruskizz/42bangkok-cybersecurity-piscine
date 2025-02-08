#!/bin/bash
#
# Use for tor client only !!
#
# Authenticate client to Tor on terminal
# 1. Initialize tor
tor
# 2. make dir <ClientOnionAuthDir>
mkdir -p /var/lib/tor/onion_auth
# 3. copy auth_private to <ClientOnionAuthDir>
cp auth/client.auth_private /var/lib/tor/onion_auth
# 4. Stop and start with client config
kill -9 $(ps | grep tor | awk '{print $1}')
tor -f conf/client.torrc

## Final access to tor network
chmod 400 ssh/id_ed25519
torify ssh -p 4242 $USER@$ONION_SITE -i ssh/id_ed25519
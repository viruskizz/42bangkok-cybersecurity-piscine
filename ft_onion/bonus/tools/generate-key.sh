#!/bin/bash
RESET="\033[0m"
GREEN="\033[32m"
YELLOW="\033[33m"

USER=viruskizz
DIR=/tmp/cred
TOR_DIR=/var/lib/tor/bonus
PEM_KEY=$DIR/$USER.key.pem
PRIVATE_KEY=$DIR/$USER.prv.key
PUBLIC_KEY=$DIR/$USER.pub.key
SERVER_AUTH_FILE=$DIR/$USER.auth
CLIENT_AUTH_FILE=$DIR/$USER.auth_private

mkdir -p $DIR

# Generate key
openssl genpkey -algorithm x25519 -out $PEM_KEY
echo -e $GREEN"PEM key generared: $PEM_KEY"$RESET

# Private Key
cat $PEM_KEY | grep -v " PRIVATE KEY" | base64pem -d | tail --bytes=32 | base32 | sed 's/=//g' > $PRIVATE_KEY
echo -e $GREEN"private key generared: $PRIVATE_KEY"$RESET

# Public Key
openssl pkey -in $PEM_KEY -pubout | grep -v " PUBLIC KEY" | base64pem -d | tail --bytes=32 | base32 | sed 's/=//g' > $PUBLIC_KEY
echo -e $GREEN"public key generared: $PUBLIC_KEY"$RESET

# Tor server and client auth
# <56-char-onion-addr-without-.onion-part>:descriptor:x25519:<x25519 private key in base32>
ONION_SITE=$(cat $TOR_DIR/hostname)
ONION_SITE_NAME=$(echo "$ONION_SITE" | sed 's/.onion//g')

echo "descriptor:x25519:$(cat $PUBLIC_KEY)" > $SERVER_AUTH_FILE
echo "$ONION_SITE_NAME:descriptor:x25519:$(cat $PRIVATE_KEY)" > $CLIENT_AUTH_FILE
echo -e $GREEN"Tor auth key generared: $AUTH_FILE"$RESET
cp $AUTH_FILE $TOR_DIR/authorized_clients
echo -e $GREEN"Copied cred to HiddenService"$RESET
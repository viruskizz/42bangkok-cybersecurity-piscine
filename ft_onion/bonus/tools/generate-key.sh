#!/bin/bash
CLIENT=viruskizz
DIR=$(dirname $0)
PEM_KEY=$DIR/cred/$CLIENT.prv.pem
PRIVATE_KEY=$DIR/cred/$CLIENT.prv.key
PUBLIC_KEY=$DIR/cred/$CLIENT.pub.key
AUTH_FILE=$DIR/cred/$CLIENT.auth

mkdir -p $DIR/cred

# Generate key
openssl genpkey -algorithm x25519 -out $PEM_KEY

# Private Key
cat $PEM_KEY | grep -v " PRIVATE KEY" | base64pem -d | tail --bytes=32 | base32 | sed 's/=//g' > $PRIVATE_KEY

# Public Key
openssl pkey -in $PEM_KEY -pubout | grep -v " PUBLIC KEY" | base64pem -d | tail --bytes=32 | base32 | sed 's/=//g' > $PUBLIC_KEY

echo "descriptor:x25519:$(cat $PUBLIC_KEY)" > $AUTH_FILE
#!/bin/bash
ONION_SITE=""
USER="viruskizz"
PORT=4242
# 1 Start to server
tor &

# 2. ssh to server
torify ssh -p $PORT "$USER@$ONION_SITE"
#!/bin/bash
mkdir -p /tmp/ssh
ssh-keygen -q -t ed25519 -N '' -f /tmp/ssh/id_ed25519

mkdir -p ~/.ssh
touch ~/.ssh/authorized_keys
cat /tmp/ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
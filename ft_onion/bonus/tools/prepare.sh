#!/bin/bash
DIR=$(dirname $0)
# Install revalant package
apt install -y basez torsocks

# Generate key
bash $DIR/generate-key.sh

#!/bin/bash
tor -f /etc/tor/torrc & \
nginx -g "daemon off;"
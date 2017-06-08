#!/bin/sh

while true; do
    ping -c1 mysql > /dev/null && break
    sleep 1
    echo "Waiting for mysql to start"
done

python3 server.py start

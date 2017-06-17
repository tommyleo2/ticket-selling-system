#!/bin/sh

until nc -z -v -w30 database 3306
do
    echo "Waiting for database connection..."
    # wait before check again
    sleep 1
done

python3 server.py ${TICKET_SERVER_CMD}

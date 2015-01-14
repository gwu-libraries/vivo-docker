#!/bin/bash

docker run -d \
    --name "vivo_db" \
    -e MYSQL_ROOT_PASSWORD=GHr54sfflsE \
    -e MYSQL_DATABASE=vivo \
    -e MYSQL_USER=vivo_user \
    -e MYSQL_PASSWORD=ghE35fkEm4 \
    gwul/vivo_db

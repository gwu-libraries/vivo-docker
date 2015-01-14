#!/bin/bash

docker run -d --name "vivo_tomcat" \
    --volumes-from vivo_app \
    -p 8080:8080 \
    --link vivo_db:db \
    -e MYDOMAIN=gwu.edu \
    gwul/vivo_tomcat

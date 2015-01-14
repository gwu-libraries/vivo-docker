#!/bin/bash

docker run -d --name "vivo_load" \
    --volumes-from vivo_app \
    --link vivo_tomcat:tomcat \
    -v ~/Data/vivo/vivo-load:/usr/local/vivo-load \
    -p 8081:80 \
    gwul/vivo_load

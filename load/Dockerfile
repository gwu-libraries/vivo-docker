#Basing on apache because need it to expose files for sparql load.
FROM httpd:latest
MAINTAINER Justin Littman <justinlittman@gwu.edu>

RUN apt-get update && apt-get install -y \
    python-dev \
    python-pip \
    lib32z1-dev \
    libxml2-dev \
    libxslt1-dev
#Upgrade pip
RUN pip install -U pip
#Preload requirements. Will need a better way to do this.
RUN pip install rdflib
RUN pip install xlrd
ENV LC_ALL C.UTF-8
WORKDIR /usr/local/vivo-load
VOLUME ["/usr/local/vivo/graphs"]
CMD pip install -r requirements.txt && httpd -DFOREGROUND

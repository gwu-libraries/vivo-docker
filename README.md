Docker for VIVO
---------------

This project contains code for dockerizing [VIVO](http://vivoweb.org).

In particular, it supports creating the following containers:

* app:  Compiles and deploys the VIVO application.
* app-local:  Extends app with GWU specific configuration, including a local ontology.  This can be used as an example for extending the app image for local setting (although the app image can be used by itself without extension).
* db:  Instantiates a MySQL db.
* tomcat:  Instantiates an instance of Tomcat for the app to run in.
* load:  Provides an environment for loading VIVO.

[app](https://registry.hub.docker.com/u/gwul/vivo_app/), [db](https://registry.hub.docker.com/u/gwul/vivo_db/), and [tomcat](https://registry.hub.docker.com/u/gwul/vivo_tomcat/) are available from Docker Hub.

Quick Start
=========
1.  [Install](https://docs.docker.com/installation/#installation) Docker.
2.  [Install](http://docs.docker.com/compose/install/) Docker Compose. 
3.  Fetch the docker-compose.yml:

    curl -L https://github.com/gwu-libraries/vivo-docker/raw/master/example.1_8_1.docker-compose.yml > docker-compose.yml

4.  Set your domain:

    export MYDOMAIN=gwu.edu

5.  Up:

    docker-compose up -d

6.  Wait.  The first time you run, you'll need to wait for the Docker images to download.  Every time you run, you'll need to wait for VIVO to start, which can take several minutes (or more).  Open a browser to http://localhost:8080/vivo.  You can log in with email vivo_root@MYDOMAIN (e.g., vivo_root@gwu.edu) and password "rootPassword".  (You'll be prompted to change the password.)

Running containers
==================
The recommended approach to starting containers is to use Docker Compose.  

Container-specific notes
========================

### app container:

* The app container can be extended with local configuration.  See app-local as an example for how it is extended at GWU.
* Host the volumes:
    * /usr/local/tomcat/webapps
    * /usr/local/vivo/home

### tomcat app:

* Complete control is available over VIVO's runtime properties.  At the very
least, your domain must be provided as the MYDOMAIN environment variable.  
Additional runtime properties can be overridden by providing as environment
variables.  See tomcat/prop_util/prop_util.py.
* Tomcat's memory can be set using the CATALINA_OPTS environment variable.
* Starting up the VIVO application in Tomcat takes a long time.  As in several
excruciating minutes.
* Once the VIVO application is running, you will be required to change the root
password.  The default username is "vivo_root@yourinstitution.edu" and password
is "rootPassword".
* VIVO performs a series of smoke tests when starting up.  You may be warned if
SMTP is not available for sending email.

### load app:

* The load app includes an instance of Apache to support a SPARQL load.
* The load app shares a local directory with the container.  This is intended to contain
the load code and can be specified in `container.sh`.
* To use the load app to execute load code, create a bash shell with `docker exec -it vivo_load /bin/bash`.

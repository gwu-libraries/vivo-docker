FROM mysql:5.7
MAINTAINER Justin Littman <justinlittman@gwu.edu>

ADD my.cnf /etc/mysql/
#https://github.com/docker-library/mysql/commit/d6268ace61047c74468d7c59b4d8da6be5dec16a caused
#mysqld to run as root.  This sets as mysql user.
CMD ["mysqld", "--user=mysql", "--datadir=/var/lib/mysql"]

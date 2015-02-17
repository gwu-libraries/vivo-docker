FROM gwul/vivo_app
MAINTAINER Justin Littman <justinlittman@gwu.edu>

ADD gwlocal.n3 /tmp/vivo-rel-1.7/rdf/tbox/filegraph/
RUN mkdir /tmp/vivo-rel-1.7/vitro-core/webapp/rdf/auth/firsttime
ADD users.n3 /tmp/vivo-rel-1.7/vitro-core/webapp/rdf/auth/firsttime/
ADD addl_permission_config.n3 /tmp/vivo-rel-1.7/vitro-core/webapp/rdf/auth/everytime/
#ADD menu.n3 /tmp/vivo-rel-1.7/rdf/display/firsttime/

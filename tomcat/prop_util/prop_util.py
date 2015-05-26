from pyjavaproperties import Properties
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: python prop_util.py <path to runtime.properties> <mydomain replacement>"
        sys.exit(1)
    runtime_filepath = sys.argv[1]
    print "Updating %s" % runtime_filepath
    p = Properties()
    p.load(open(runtime_filepath))
    print "****Properties before****"
    p.list()
    #Add/replace environment variables that begin with v_
    for key, value in [(key[2:], os.environ[key]) for key in os.environ if key.startswith("v_")]:
        print "Adding key %s: %s" % (key, value)
        p[key] = value
    #Replace mydomain in any values
    newdomain = sys.argv[2]
    for key, value in [(key, value) for (key, value) in p.iteritems() if "mydomain.edu" in value]:
        new_value = value.replace("mydomain.edu", newdomain)
        print "Changing key %s from %s to %s" % (key, value, new_value)
        p[key] = new_value
    #Only set email keys if env var present.
    if os.environ.get('VIVO_EMAIL', False) != "true":
        print "Removing email settings."
        p['email.smtpHost'] = ""
        p['email.replyTo'] = ""
    #Set DB values based on docker-provided environment variables
    p['VitroConnection.DataSource.url'] = "jdbc:mysql://db/%s" % os.getenv('DB_ENV_MYSQL_DATABASE')
    p['VitroConnection.DataSource.username'] = os.getenv('DB_ENV_MYSQL_USER')
    p['VitroConnection.DataSource.password'] = os.getenv('DB_ENV_MYSQL_PASSWORD')
    print "****Properties after****"
    p.list()
    p.store(open(runtime_filepath,'w'))

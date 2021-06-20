# Simple JDBC client - get entries from a table
# Add ojdbc14.jar to the classpath

# jython imports
import sys
from com.ziclix.python.sql import zxJDBC

# java imports

DB_DRIVER = 'oracle.jdbc.OracleDriver'

def usage(argv):
    if len(argv) < 3:
        print 'Usage:'
        print '\tjython getdbmetadata.py <JDBC_URL> <USER> <PASSWORD>'
        print '\tJDBC URL format: jdbc:oracle:thin:@DBHOST:DBPORT:DBSID'
        sys.exit(0)

def main(argv):
    usage(argv)

    jdbc_url = argv[1]
    user = argv[2]
    password = argv[3]

    db = zxJDBC.connect(jdbc_url, user, password, DB_DRIVER)

    cursor = db.cursor()
    query = 'select usr_login, usr_first_name, usr_last_name from usr'
    cursor.execute(query)

    lst = cursor.fetchall()

    for elem in lst:
	print elem
 
    cursor.close()
    db.close()

# main method
if __name__ == '__main__':
    usage(sys.argv)
    main(sys.argv)

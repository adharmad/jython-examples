# Gets datebase metadata including table names and their column names
# Add ojdbc14.jar to the classpath

# jython imports
import sys
from com.ziclix.python.sql import zxJDBC

# java imports

#DB_DRIVER = 'oracle.jdbc.driver.OracleDriver'
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
 
    name = db.dbname
    version = db.dbversion

    print 'dbname = ', name
    print 'version = ', version    

    cursor.tables(None, user, '%', None)
    tables = cursor.fetchall()

    for table in tables:
        tableName = table[2]
        print tableName

        cursor.columns(None, user, tableName, '%')
        columns = cursor.fetchall()

        for col in columns:
            colName = col[3]
            colType = col[5] 

            print '\t' + colName + ' - \t' + colType

    cursor.close()
    db.close()

# main method
if __name__ == '__main__':
    usage(sys.argv)
    main(sys.argv)

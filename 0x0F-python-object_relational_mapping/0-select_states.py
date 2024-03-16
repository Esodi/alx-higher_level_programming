#!/usr/bin/python3

import MySQLdb
import sys

def list_states(mysql_username, mysql_password, database_name):
    db = MySQLdb.connect(host='localhost', user=mysql_username, passwd=mysql password, port='3306', db=database_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id asc")
    states = cur.fetchall()
    for i in states:
        print('({}, {})'.format(i[0], i[1]))

if __name__ == '__main__':
    if (len sys.argv) != 4:
        print('wrong');
    else:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])

#!/usr/bin/python3
'''
    a script that lists all states from the database hbtn_0e_0_usa.

'''

import MySQLdb
import sys

def list_states(mysql_username, mysql_password, database_name):
    ''' a function that proccesses an output'''
    db = MySQLdb.connect(host='localhost', user=mysql_username, passwd=mysql_password, port=3306, db=database_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cur.fetchall()
    for i in states:
        print('({}, {})'.format(i[0], i[1]))
    cur.close()
    db.close()

if __name__ == '__main__':
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])

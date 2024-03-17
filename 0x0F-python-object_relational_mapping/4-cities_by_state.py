#!/usr/bin/python3
'''
     a script that lists all cities from the database hbtn_0e_4_usa.

'''

import sys
import MySQLdb

def allcities(username, password, database):
    '''function that process an output'''
    db = MySQLdb.connect(host='localhost', passwd=password, user=username, db=database)
    cur = db.cursor()
    cur2 = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY cities.id ASC")
    cur2.execute("SELECT * FROM states ORDER BY id ASC")
    fetch = cur.fetchall()
    fetch2 = cur2.fetchall()
    for i in fetch:
        print('({})'.format(i))
    cur.close()
    db.close()

if __name__ == '__main__':
    allcities(sys.argv[1], sys.argv[2], sys.argv[3])

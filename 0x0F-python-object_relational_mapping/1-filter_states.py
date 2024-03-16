#!/usr/bin/python3
'''
     a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa

'''

import sys
import MySQLdb

def list_Ns(username, password, dbname):
    '''a function that process an output'''
    db = MySQLdb.connect(host='localhost', user=username, passwd=password, port=3306, db=dbname)
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id asc"
    cur.execute(sql)
    fetchedNs = cur.fetchall()
    for i in fetchedNs:
        print(f'({i[0]}, {i[1]})')
    cur.close()
    db.close()

if __name__ == '__main__':
    list_Ns(sys.argv[1], sys.argv[2], sys.argv[3])

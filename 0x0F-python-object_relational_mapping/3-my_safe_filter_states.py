#!/usr/bin/python3
'''
    a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

'''

import sys
import MySQLdb

def list_Name(username, password, dbname, state_name):
    '''function that proccesses an input'''
    db = MySQLdb.connect(host='localhost', user=username, port=3306, passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (state_name,))
    fetch = cur.fetchall()
    for i in fetch:
        print('({}, {})'.format(i[0], i[1]))
    cur.close()
    db.close()

if __name__ == '__main__':
    list_Name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

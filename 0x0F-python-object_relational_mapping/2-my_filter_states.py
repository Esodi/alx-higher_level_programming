#!/usr/bin/python3
'''
    a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

'''

import sys
import MySQLdb

def list_Name(username, password, dbname, state_name):
    ''' a function that proccesses an output'''
    db = MySQLdb.connect(host='localhost', user=username, passwd=password, port=3306, db=dbname)
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name = 'Arizona'"
    cur.execute(sql)
    fetch = cur.fetchall()
    for i in fetch:
        print(f'({i[0]}, {i[1]}')
    cur.close()
    db.close()

if __name__ == '__main__':
    list_Name(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])

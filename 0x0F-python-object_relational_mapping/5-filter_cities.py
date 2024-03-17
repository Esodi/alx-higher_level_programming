#!/usr/bin/python3
'''
    a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa.

'''

import sys
import MySQLdb

def allcitiesv2(username, password, dbname, state_name):
    '''a function that processes an output'''
    db = MySQLdb.connect(host='localhost', user=username, port=3306, db=dbname, passwd=password)
    cur = db.cursor()
    sql = "SELECT states.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(sql, (state_name,))
    fetch = cur.fetchall()
    for i in fetch:
        print('{}'.format(i))
    cur.close()
    db.close()

if __name__ == '__main__':
    allcitiesv2(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

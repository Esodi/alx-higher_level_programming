#!/usr/bin/python3
'''
    displays all values in the states table where name matches the argument.

'''


import sys
import MySQLdb


def list_Name(username, password, dbname, state_name):
    ''' a function that proccesses an output'''
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            port=3306,
            db=dbname
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' COLLATE utf8mb4_bin".format(state_name,))
    fetch = cur.fetchall()
    for i in fetch:
        print('{}'.format(i))
    cur.close()
    db.close()


if __name__ == '__main__':
    list_Name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

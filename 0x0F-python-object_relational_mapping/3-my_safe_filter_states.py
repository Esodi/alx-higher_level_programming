#!/usr/bin/python3
'''
    write one that is safe from MySQL injections!

'''


import sys
import MySQLdb


def list_Name(username, password, dbname, state_name):
    '''function that proccesses an input'''
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            port=3306,
            passwd=password,
            db=dbname
            )
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name = {}".format("%s")
    cur.execute(sql, (state_name,))
    fetch = cur.fetchall()
    for i in fetch:
        print('{}'.format(i))
    cur.close()
    db.close()


if __name__ == '__main__':
    list_Name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

#!/usr/bin/python3
'''
     a script that lists all cities from the database hbtn_0e_4_usa.

'''


import sys
import MySQLdb


def allcities(username, password, database):
    '''function that process an output'''
    db = MySQLdb.connect(
            host='localhost',
            passwd=password,
            user=username,
            db=database
            )
    cur = db.cursor()
    cur.execute("
                SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states
                ON cities.state_id=states.id
                ORDER BY cities.id
                ASC"
                )
    fetch = cur.fetchall()
    for i in fetch:
        print('{}'.format(i))
    cur.close()
    db.close()


if __name__ == '__main__':
    allcities(sys.argv[1], sys.argv[2], sys.argv[3])

#!/usr/bin/python3
'''
     all states with a name starting with N from the database hbtn_0e_0_usa

'''


import sys
import MySQLdb


def list_Ns(username, password, dbname):
    '''a function that process an output'''
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            port=3306,
            db=dbname
            )
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name LIKE 'N%' COLLATE utf8mb4_bin ORDER BY states.id ASC"
    cur.execute(sql)
    fetchedNs = cur.fetchall()
    for i in fetchedNs:
        print(f'{i}')
    cur.close()
    db.close()


if __name__ == '__main__':
    list_Ns(sys.argv[1], sys.argv[2], sys.argv[3])

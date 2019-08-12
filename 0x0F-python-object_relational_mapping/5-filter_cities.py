#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name\
                 FROM cities\
                 LEFT JOIN states ON cities.state_id=states.id\
                 WHERE states.name LIKE BINARY %s\
                 ORDER BY cities.id ASC", (sys.argv[4],))
    query_rows = cur.fetchall()
    print(', '.join([row[0] for row in query_rows]))
    cur.close()
    conn.close()

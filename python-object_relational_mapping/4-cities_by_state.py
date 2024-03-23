#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    """Connect to the databse"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

    """Create a cursor object"""
    cur = db.cursor()

    """Execute a sql query"""
    cur.execute("SELECT cities.id, cities.name,\
                states.name FROM cities INNER JOIN states ON\
                cities.state_id = states.id ORDER BY cities.id")

    """Fetch all rows"""
    for row in cur.fetchall():
        print(row)

    """Close cursor and db"""
    cur.close()
    db.close()
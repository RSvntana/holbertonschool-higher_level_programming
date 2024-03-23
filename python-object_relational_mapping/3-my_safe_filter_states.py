#!/usr/bin/python3
""" write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Connect to the dabatabase"""
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

    """Create a cursor object"""
    cur = db.cursor()

    """acreate the query and get the state
    name from the command line
    Like BINARY is used to make the search case sensitive"""
    query = "SELECT * FROM states WHERE name LIKE BINARY \
        %s ORDER BY states.id ASC"

    """Execute the query"""
    cur.execute(query, (sys.argv[4],))

    """Fetch all rows"""
    for row in cur.fetchall():
        print(row)

    """Close cursor and db"""
    cur.close()
    db.close()
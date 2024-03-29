#!/usr/bin/python3
"""takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument"""


import MySQLdb as sql
from sys import argv
if __name__ == '__main__':
    db = sql.connect(host="localhost",
                     port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
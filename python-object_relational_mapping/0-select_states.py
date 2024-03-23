#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes three command line arguments: MySQL username,
password, and database name.
"""

# Import necessary modules
import MySQLdb
import sys
"""This condition checks if the script is being run
directly or imported as a module
The code inside this condition will only run if the
script is run directly"""
if __name__ == "__main__":
    """ Establish a connection to the MySQL database
    sys.argv[1], sys.argv[2], and sys.argv[3] are command
    line arguments for MySQL username, password, and database name"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

# Create a cursor object to execute SQL queries
    cur = db.cursor()

# Execute a SQL query to select all states from the database,
#  ordered by states.id in ascending order
    cur.execute(
        "SELECT states.id, states.name FROM states ORDER BY states.id ASC")

# Fetch all rows from the result of the query
    rows = cur.fetchall()

# Loop through each row and print it
    for row in rows:
        print(row)

# Close the cursor and the database connection
    cur.close()
    db.close()
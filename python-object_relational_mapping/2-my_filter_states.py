#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # Build query with format (user input)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        sys.argv[4]
    )
    cursor.execute(query)

    # Fetch all matching rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()

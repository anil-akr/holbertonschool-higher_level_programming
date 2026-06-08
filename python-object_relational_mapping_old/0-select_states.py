#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to database using arguments provided at command line
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor to execute SQL queries
    cursor = db.cursor()

    # Execute query and sort by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results
    rows = cursor.fetchall()

    # Print results in the required format
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()

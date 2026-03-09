#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Access arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the executed query
    query_rows = cursor.fetchall()

    # Print each row in the specified format
    for row in query_rows:
        print(row)

    # Clean up: close the cursor and the database connection
    cursor.close()
    db.close()

#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def list_all_states():
    """
    Connects to the MySQL database and lists all states.
    """
    # Connect to MySQL server
    db_connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],  # MySQL username
            passwd=sys.argv[2],  # MySQL password
            db=sys.argv[3]  # Database name
    )

    # Create cursor
    db_cursor = db_connection.cursor()

    # Execute SQL query to select all states
    db_cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all states
    states = db_cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # close cursor and connection
    db_cursor.close()
    db_connection.close()


if __name__ == "__main__":
    list_all_states()

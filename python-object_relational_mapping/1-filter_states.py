#!/usr/bin/python3
"""
Script that list all states with a name starting with 'N' from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def list_states_starting_with_N():
    """
    Connects to the MySQL database and lists all states whose names start with 'N'.
    """
    # Connect to MySQL server
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1], # MySQL username
        passwd=sys.argv[2], # MySQL password
        db=sys.argv[3] # Database name
    )

    # Create cursor
    db_cursor = db_connection.cursor()

    # Execute SQL query to select states starting with 'N'
    db_cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id")

    # Fetch all matching states
    matching_states = db_cursor.fetchall()

    # Print the results
    for state in matching_states:
        print(state)

    # Close cursor and connection
    db_cursor.close()
    db_connection.close()


if __name__ == "__main__":
    list_states_starting_with_N()

#!/usr/bin/python3
"""
Script to query and display values from the states table of hbtn_0e_0_usa
where the name matches the specified argument, using parameterized queries
to prevent SQL injection attacks.
"""
import MySQLdb
import sys


def query_states_by_name_safely():
    """
    Connects to the MySQL database and retrieves states where the name matches
    the specified argument using parameterized queries to prevent SQL injection.
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

    # Define SQL command with parameterized query
    sql_command = "SELECT * FROM states WHERE name = %s ORDER BY id"

    # Execute SQL command with argument tuple to prevent SQL injection
    db_cursor.execute(sql_command, (sys.argv[4],))

    # Fetch matching states
    matching_states = db_cursor.fetchall()

    # Print the results
    for state in matching_states:
        print(state)

    # Close cursor and connection
    db_cursor.close()
    db_connection.close()


if __name__ == "__main__":
    query_states_by_name_safely()

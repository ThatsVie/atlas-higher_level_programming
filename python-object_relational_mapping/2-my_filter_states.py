#!/usr/bin/python3
"""
Script to query and display values from the states table of hbtn_0e_0_usa
where the name matches a specified argument.
"""
import MySQLdb
import sys


def filter_states():
    """
    Connects to the MySQL database and retrieves states where the name matches
    the specified argument, then displays the results.
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

    # Execute SQL query to select states where the name matches the argument
    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' "
                      "ORDER BY id".format(sys.argv[4]))

    # Fetch matching states
    matching_states = db_cursor.fetchall()

    # Print the results
    for state in matching_states:
        print(state)

    # Close cursor and connection
    db_cursor.close()
    db_connection.close()


if __name__ == "__main__":
    filter_states()

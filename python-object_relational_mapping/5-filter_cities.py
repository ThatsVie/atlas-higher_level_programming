#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


def list_all_cities_by_state():
    """ List all cities by state name """

    # Connect to MySQL database
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],  # MySQL username
        passwd=sys.argv[2],  # MySQL password
        db=sys.argv[3]  # Database name
    )

    # Create a cursor object
    db_cursor = db_connection.cursor()

    # Execute SQL query to select cities by state name
    db_cursor.execute("SELECT cities.name \
                       FROM cities \
                       INNER JOIN states ON cities.state_id = states.id \
                       WHERE states.name = %s \
                       ORDER BY cities.id ASC", (sys.argv[4],))

    # Fetch the results of the query
    cities = db_cursor.fetchall()

    # Print the list of cities separated by commas
    print(", ".join([city[0] for city in cities]))

    # Close the cursor and database connection
    db_cursor.close()
    db_connection.close()


if __name__ == "__main__":
    list_all_cities_by_state()

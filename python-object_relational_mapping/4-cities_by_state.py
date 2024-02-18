#!/usr/bin/python3
"""
Script that list all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_all_cities():
    """
    Connects to the MySQL database and retrieves all cities,
    including their corresponding state names, then displays the results.
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

    # Execute SQL query to select all cities with their corresponding state names
    sql_query = "SELECT cities.id, cities.name, states.name " \
                "FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id"

    db_cursor.execute(sql_query)

    # Fetch all cities and their corresponding state names
    city_data = db_cursor.fetchall()

    # Print the results
    for city in city_data:
        print(city)

    # Close cursor and connection
    db_cursor.close()
    db_connection.close()


if __name__ == "__main__":
    list_all_cities()

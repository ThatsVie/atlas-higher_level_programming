# SQL - Introduction

This repository contains a series of SQL scripts that demonstrate basic operations in MySQL server. Each script performs a specific task related to database management, such as listing databases and tables, creating and deleting databases and tables, inserting and querying data, and performing data manipulation and analysis.

## List of Files

1. **0-list_databases.sql**: Script that lists all databases of MySQL server.
2. **1-create_database_if_missing.sql**: Script that creates the database hbtn_0c_0 in MySQL server if it doesn't already exist.
3. **2-remove_database.sql**: Script that deletes the database hbtn_0c_0 in MySQL server if it exists.
4. **3-list_tables.sql**: Script that lists all the tables of a database in MySQL server.
5. **4-first_table.sql**: Creates a table called first_table in the current database in MySQL server.
6. **5-full_table.sql**: Script that prints the description of the table first_table from the database hbtn_0c_0 in MySQL server.
7. **6-list_values.sql**: Script that lists all rows of the table first_table from the database hbtn_0c_0 in MySQL server.
8. **7-insert_value.sql**: Script that inserts a new row in the table first_table (database hbtn_0c_0) in MySQL server.
9. **8-count_89.sql**: Script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in MySQL server.
10. **9-full_creation.sql**: Script that creates a table second_table in the database hbtn_0c_0 in MySQL server and adds multiple rows.
11. **10-top_score.sql**: Script that lists all records of the table second_table of the database hbtn_0c_0 in MySQL server, ordered by score (top first).
12. **11-best_score.sql**: Script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in MySQL server, ordered by score (top first).
13. **12-no_cheating.sql**: Script that updates the score of Bob to 10 in the table second_table.
14. **13-change_class.sql**: Script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in MySQL server.
15. **14-average.sql**: Script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in MySQL server.
16. **15-groups.sql**: Script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in MySQL server, grouped by score.
17. **16-no_link.sql**: Script that lists all records of the table second_table of the database hbtn_0c_0 in MySQL server, excluding rows without a name value.

## Usage

To execute these scripts, you need to have access to a MySQL server and the necessary permissions to create and modify databases and tables. You can run these scripts using a MySQL client, passing the appropriate arguments as required by each script.

For example, to list all databases, you can execute:
mysql -u <username> -p <password> -e "source 0-list_databases.sql"

Replace `<username>` and `<password>` with your MySQL credentials.

Similarly, you can execute other scripts by replacing the script file name and providing the required arguments.


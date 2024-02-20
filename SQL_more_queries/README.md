# SQL - More Queries

This repository contains SQL scripts for advanced queries and database management tasks in MySQL. These scripts cover a range of operations such as managing user privileges, creating tables, querying data, and performing joins and subqueries.

## Files

1. **0-privileges.sql**: Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the localhost server.
2. **1-create_user.sql**: Creates the MySQL server user `user_0d_1` with all privileges and sets the password.
3. **2-create_read_user.sql**: Creates the database `hbtn_0d_2` and the user `user_0d_2` with read-only privileges.
4. **3-force_name.sql**: Creates a table `force_name` on the MySQL server.
5. **4-never_empty.sql**: Creates a table `id_not_null` with a default value constraint.
6. **5-unique_id.sql**: Creates a table `unique_id` with a unique identifier constraint.
7. **6-states.sql**: Creates the database `hbtn_0d_usa` and the `states` table within it.
8. **7-cities.sql**: Creates the database `hbtn_0d_usa` and the `cities` table within it, establishing a foreign key constraint.
9. **8-cities_of_california_subquery.sql**: Lists all cities of California from the `cities` table using a subquery.
10. **9-cities_by_state_join.sql**: Lists all cities from the `cities` table along with their corresponding states using a join.
11. **10-genre_id_by_show.sql**: Lists all shows from the `tv_shows` table along with their associated genre IDs.
12. **11-genre_id_all_shows.sql**: Lists all shows from the `tv_shows` table along with their associated genre IDs, including those without a genre.
13. **12-no_genre.sql**: Lists all shows without a genre from the `tv_shows` table.
14. **13-count_shows_by_genre.sql**: Lists all genres from the `tv_genres` table along with the number of shows linked to each.
15. **14-my_genres.sql**: Lists all genres of the show "Dexter" from the `tv_shows` table.
16. **15-comedy_only.sql**: Lists all comedy shows from the `tv_shows` table.
17. **16-shows_by_genre.sql**: Lists all shows along with their linked genres from the `tv_shows` table.

## Usage

1. Ensure you have MySQL installed and running.
2. Execute each SQL script using a MySQL client or command-line tool, ensuring any required databases are created and any necessary user privileges are granted.

1. **Check and Grant Privileges**: 
   
    ```bash
    guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    ```

2. **Create Users with Specific Privileges**:

    ```bash
    guillaume@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    ```

3. **Ensure Specific Table Constraints**:

    ```bash
    guillaume@ubuntu:~/$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ cat 6-states.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ cat 7-cities.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    ```

4. **Fetch Data**:

    ```bash
    guillaume@ubuntu:~/$ cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
    Enter password: 
    ```

    ```bash
    guillaume@ubuntu:~/$ cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
    Enter password: 
    ```

Replace `root` with your MySQL username and password if required. Ensure appropriate permissions to execute the commands.

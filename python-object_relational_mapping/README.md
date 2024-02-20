# Python - Object Relational Mapping

This repository contains scripts written in Python for performing Object Relational Mapping (ORM) tasks using SQLAlchemy with MySQL databases. Each script serves a specific purpose and interacts with the database to perform various operations.

## Files

1. **0-select_states.py**:
   - Script that lists all states from the database `hbtn_0e_0_usa`.
  
2. **1-filter_states.py**:
   - Script that lists all states with a name starting with 'N' from the database `hbtn_0e_0_usa`.

3. **2-my_filter_states.py**:
   - Script to query and display values from the states table of `hbtn_0e_0_usa` where the name matches a specified argument.

4. **3-my_safe_filter_states.py**:
   - Script to query and display values from the states table of `hbtn_0e_0_usa` where the name matches the specified argument, using parameterized queries to prevent SQL injection attacks.

5. **4-cities_by_state.py**:
   - Script that lists all cities from the database `hbtn_0e_4_usa`.

6. **5-filter_cities.py**:
   - Script that takes in the name of a state as an argument and lists all cities of that state, using the database `hbtn_0e_4_usa`.

7. **6-model_state.py**:
   - Defines the State class and the declarative base for SQLAlchemy.

8. **7-model_state_fetch_all.py**:
   - Script to list all State objects from the database `hbtn_0e_6_usa`.

9. **8-model_state_fetch_first.py**:
   - Script that prints the first State object from the database `hbtn_0e_6_usa`.

10. **9-model_state_filter_a.py**:
    - Script that lists all State objects that contain the letter 'a' from the database `hbtn_0e_6_usa`.

11. **10-model_state_my_get.py**:
    - Script that prints the State object with the name passed as an argument from the database `hbtn_0e_6_usa`.

12. **11-model_state_insert.py**:
    - Script that adds the State object 'Louisiana' to the database `hbtn_0e_6_usa`.

13. **12-model_state_update_id_2.py**:
    - Script that changes the name of a State object from the database `hbtn_0e_6_usa`.

14. **13-model_state_delete_a.py**:
    - Script that deletes all State objects with a name containing the letter 'a' from the database `hbtn_0e_6_usa`.

15. **14-model_city_fetch_by_state.py**:
    - Script that prints all City objects from the database `hbtn_0e_14_usa`.

## SQL Files

1. **0-select_states.sql**:
   - SQL script to create the states table in `hbtn_0e_0_usa` with some data.

2. **4-cities_by_state.sql**:
   - SQL script to create the database `hbtn_0e_4_usa`, tables states and cities, along with some data.

3. **6-model_state.sql**:
   - SQL script to create the database `hbtn_0e_6_usa`.

4. **7-model_state_fetch_all.sql**:
   - SQL script to insert states into `hbtn_0e_6_usa`.

5. **14-model_city_fetch_by_state.sql**:
   - SQL script to create the database `hbtn_0e_14_usa`, tables states and cities, along with some data.

## Python Modules

1. **model_state.py**:
   - Contains the definition of the State class and the declarative base for SQLAlchemy.

2. **model_city.py**:
   - Contains the class definition of a City, which inherits from the Base class, and an instance Base = declarative_base().

## Usage

This section provides instructions on how to run the Python scripts and execute the SQL scripts provided in the repository. It also includes examples of command-line usage for running the Python scripts with appropriate arguments.

To run any of the Python scripts in this repository, you need to have Python3 installed on your system along with MySQL 8.0, MySQLdb module version 2.0.x, and SQLAlchemy module version 1.4.x

### Running Python Scripts
**Clone this repository to your local machine:**

```bash
   git clone https://github.com/ThatsVie/atlas-higher_level_programming.git
```

**Navigate to the directory containing the script you want to run:**
   
```bash
python-object_relational_mapping
```

**Run the desired Python script with the appropriate command-line arguments. For example:**

```bash
./0-select_states.py <db_username> <db_password> <db_name>
```

Replace <db_username>, <db_password>, and <db_name> with your MySQL database credentials and database name, respectively.


### SQL Scripts
If you want to create the necessary databases and tables using the SQL scripts provided, you can execute them using a MySQL client such as mysql or any MySQL GUI tool.

```bash
mysql -u username -p < 0-select_states.sql
```

Replace username with your MySQL username.


**These usage examples demonstrate how to execute SQL scripts to create and manipulate database tables and how to use Python scripts to interact with the database and retrieve specific data, along with the expected outputs where applicable:**


**Create states table in hbtn_0e_0_usa with some data**

```bash
guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password:
```

 **Fetch all states from hbtn_0e_0_usa**

```bash
guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```

**Filter states by name using a Python script**

```bash
guillaume@ubuntu:~/$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
```

**Filter states by name using a Python script**

```bash
guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

**Filter states by name using a Python script with SQL injection protection**

```bash
guillaume@ubuntu:~/$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

**Create states and cities tables in hbtn_0e_4_usa with some data**

```bash
guillaume@ubuntu:~/$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password:
```

**Fetch all cities with their corresponding states from hbtn_0e_4_usa**

```bash
guillaume@ubuntu:~/$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
```

**Filter cities by state name using a Python script**

```bash
guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
```

**Create states table in hbtn_0e_6_usa**

```bash
guillaume@ubuntu:~/$ cat 6-model_state.sql | mysql -uroot -p
Enter password:
```

**Run Python script to create the State model**

```bash
guillaume@ubuntu:~/$ ./6-model_state.py root root hbtn_0e_6_usa
```

**Insert states into hbtn_0e_6_usa using SQL**

```bash
guillaume@ubuntu:~/$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password:
```

**Fetch all states from hbtn_0e_6_usa using Python**

```bash
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
```

**Fetch the first state from hbtn_0e_6_usa using Python**

```bash
guillaume@ubuntu:~/$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
```

**Filter states containing letter 'a' from hbtn_0e_6_usa using Python**
```bash
guillaume@ubuntu:~/$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
```

**Get state ID by name from hbtn_0e_6_usa using Python**

```bash
guillaume@ubuntu:~/$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
```

**Insert a new state into hbtn_0e_6_usa using Python**

```bash
guillaume@ubuntu:~/$ ./11-model_state_insert.py root root hbtn_0e_6_usa
6
```

**Fetch all states from hbtn_0e_6_usa after insertion**
```bash
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
```

**Update state name with ID 2 in hbtn_0e_6_usa using Python**

```bash
guillaume@ubuntu:~/$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa
```

**Fetch all states from hbtn_0e_6_usa after update**

```bash
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
2: New Mexico
4: New York
```

**Delete states containing letter 'a' from hbtn_0e_6_usa using Python**

```bash
guillaume@ubuntu:~/$ ./13-model_state_delete_a.py root root hbtn_0e_6_usa
```

**Fetch all states from hbtn_0e_6_usa after deletion**

```bash
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
2: New Mexico
4: New York
```

**Create states and cities tables in hbtn_0e_14_usa with some data**

```bash
guillaume@ubuntu:~/$ cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
Enter password:
```

**Fetch all cities with their corresponding states from hbtn_0e_14_usa using Python**

```bash
guillaume@ubuntu:~/$ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
```

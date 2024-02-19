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

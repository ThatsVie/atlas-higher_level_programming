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

Below is a step-by-step guide on how to interact with an SQL database using various SQL scripts along with the expected output. Each section demonstrates a specific action, such as listing databases, creating databases and tables, inserting values, querying data, and more. Simply copy and paste the commands into your terminal to execute them.

**List all databases**

```bash
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys
``` 

**Create a database if it doesn't exist**
```bash
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password:
```

**Verify the database creation**

```bash
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
sys
```

**Remove a database**

```bash
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
```

**List tables in a specific database**

```bash
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables_in_mysql                                                                              
columns_priv                                                                                 
component                                                                                    
db                                                                                           
default_roles                                                                                
engine_cost                                                                                  
func                                                                                         
general_log                                                                                  
global_grants                                                                                
gtid_executed                                                                                
help_category                                                                                
help_keyword                                                                                 
help_relation                                                                                
help_topic                                                                                   
innodb_index_stats                                                                           
innodb_table_stats                                                                           
password_history                                                                             
plugin                                                                                       
procs_priv                                                                                   
proxies_priv                                                                                 
replication_asynchronous_connection_failover                                                 
replication_asynchronous_connection_failover_managed                                         
role_edges                                                                                   
server_cost                                                                                  
servers                                                                                      
slave_master_info                                                                            
slave_relay_log_info                                                                         
slave_worker_info                                                                            
slow_log                                                                                     
tables_priv                                                                                  
time_zone                                                                                    
time_zone_leap_second                                                                        
time_zone_name                                                                               
time_zone_transition                                                                         
time_zone_transition_type                                                                    
user
```

**Create a table**

```bash
guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
```

**List tables to verify creation**

```bash
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
```

**View table structure**

```bash
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table                                                                         
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
``` 

**List values in a table**

```bash
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
```

**Insert a value into the table**

```bash
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
``` 

**Verify insertion**

```bash
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
89  Best School
89  Best School
```

**Count occurrences of a value**

```bash
guillaume@ubuntu:~/$ guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password: 
3
```

**Full table creation script**

```bash
guillaume@ubuntu:~/$ guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
```

**Top score from a table**

```bash
guillaume@ubuntu:~/$ guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
8   George
3   Alex
```

**Best score from a table**

```bash
guillaume@ubuntu:~/$ guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
```

**No cheating allowed query**

```bash
guillaume@ubuntu:~/$ guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
```

**Top score after modifying data**

```bash
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
```

**Change class of a student**

```bash
guillaume@ubuntu:~/$ guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
```

**Verify class change**

```bash
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
```

**Calculate average score**

```bash
guillaume@ubuntu:~/$ guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
average
9.3333
```

**Group values by score**

```bash
guillaume@ubuntu:~/$  guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   number
10  2
8   1
```

**Query without linking tables**

```bash
guillaume@ubuntu:~/$ guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
```

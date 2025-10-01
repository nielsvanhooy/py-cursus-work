# Data Management With Python, SQLite, and SQLAlchemy

in this course we will use the following python scripts.

- ip_manager.py
- ip_manager.csv

Furthermore this course assumes you have basic knowledge of a relational database (knowing what it is.)


```python
import csv
from time import sleep


def file_opener_dict():
    return_data = []
    with open("ip_manager.csv", newline='') as csvfile:
        content = csv.DictReader(csvfile)
        for things in content:
            return_data.append(things)
    return return_data


def display_data(db_data):
    for data in db_data:
        print(data)


def entry_adder(db_data):
    new_ip_address = input("ip_address:")
    new_hostname = input("hostname:")
    new_department = input("department:")
    new_assigned_date = input("assigned_date:")
    new_notes = input("notes:")
    new_entry = {
        'ip_address': new_ip_address,
        'hostname': new_hostname,
        'department': new_department,
        'assigned_date': new_assigned_date,
        'notes': new_notes
    }
    print(f"adding: {new_entry}")
    db_data.append(new_entry)


def entry_searcher(db_data):
    lookup = str(input('find: '))
    try:
        for db_index, data in enumerate(db_data):
            for k,v in data.items():
                if (k == "ip_address" or k == "hostname") and lookup == v :
                    print(f"matched {lookup} to {k,v} on index {db_index}, from:\n{data}")
                    return db_index
        raise LookupError(f"Error between Keyboard and Screen, aka User. no {lookup} in date")
    except LookupError:
        print(f"No entry found for {lookup}")


def entry_remover(db_data, db_index):
    confirm = input("DELETE\tY/N?\t").upper()
    match confirm:
        case "Y":
            db_data.pop(db_index)
            print("deleted")
        case _:
            print("cancel")


def file_saver_new(db_data):
    with open("ip_addr.csv", "w", newline='') as csvfile:
        print("Writing to file")
        fieldnames = ['ip_address', 'hostname', 'department', 'assigned_date', 'notes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for data in db_data:
            writer.writerow(data)
            sleep(0.2)
    print("Done")


def menu():
    options = """
    0. re-import form file
    1. show all
    2. search by IP or HOSTNAME (UNDER_CONSTRUCTION)
    3. add an entry
    4. remove an entry (UNDER_CONSTRUCTION)
    5. save to file new
    6. quit
    """
    return options


def main():
    db_data = file_opener_dict()
    busy = True
    while busy:
        print(menu())
        choice = int(input('choose:'))
        match choice:
            case 0:
                db_data = file_opener_dict()
            case 1:
                display_data(db_data)
            case 2:
                entry_searcher(db_data)
            case 3:
                entry_adder(db_data)
            case 4:
                db_index = entry_searcher(db_data)
                entry_remover(db_data, db_index)
            case 5:
                file_saver_new(db_data)
            case _:
                print("\t\tBYE!")
                busy = False


if __name__ == '__main__':
    main()

```

and the csv file that comes with it:

```csv
ip_address,hostname,department,assigned_date,notes
192.168.1.10,printer01,HR,2023-01-15,Main office printer
192.168.1.20,laptop-alice,Marketing,2023-02-05,Alice's laptop
192.168.1.30,desktop-bob,Engineering,2023-03-10,Bob's workstation
192.168.1.40,server-file01,IT,2023-01-20,File server
192.168.1.50,laptop-carol,Sales,2023-02-12,Carol's laptop
192.168.1.60,desktop-dave,Accounting,2023-03-15,Dave's workstation
192.168.1.100,server-db01,IT,2023-01-10,Database server
192.168.1.101,printer02,Marketing,2023-02-18,Marketing printer
192.168.1.102,ap-conference,IT,2023-01-25,Conference room access point
192.168.1.200,router-main,IT,2023-01-05,Main office router
```

## Flat File Data Management

working with data in flat files is manageable for small datasets, but as the data grows, it becomes cumbersome to handle. 
This is where databases come into play, providing efficient data storage, retrieval, and management capabilities.

Large files are still human-readable, but editing them to create data or look for problems becomes a more difficult task. If your application will change the data in the file, then one solution would be to read the entire file into memory, make the changes, and write the data out to another file.
Another problem with using flat files is that you’ll need to explicitly create and maintain any relationships between parts of your data and the application program within the file syntax. Additionally, you’ll need to generate code in your application to use those relationships.
A final complication is that people you want to share your data file with will also need to know about and act on the structures and relationships you’ve created in the data. To access the information, those users will need to understand not only the structure of the data but also the programming tools necessary for accessing it.

our example script and accompanying csv file is a simple IP address manager. It allows you to load IP address data from a CSV file, display the data, add new entries, search for entries by IP address or hostname, remove entries, and save the updated data back to a new CSV file.
While this approach works for small datasets, it has several limitations:

- **Scalability**: As the dataset grows, loading the entire file into memory can become inefficient and slow.
- **Concurrency**: If multiple users or processes need to access or modify the data simultaneously, managing file locks and ensuring data integrity can be challenging.
- **Complex Queries**: Performing complex queries or searches on the data can be cumbersome and slow, as it requires iterating through the entire dataset.
- **Data Integrity**: Ensuring data integrity and consistency can be difficult, especially when multiple operations are performed on the data.
- **Error Handling**: Handling errors, such as file not found or data corruption, requires additional code and can complicate the application logic.

To overcome these limitations, we can use a database management system (DBMS) like SQLite, which provides a more robust and efficient way to manage data. SQLite is a lightweight, serverless, self-contained SQL database engine that is easy to set up and use.
but first we need to learn a little bit about relational databases itself.


## relational Databases

A relational database is a type of database that stores and provides access to data points that are related to one another. Relational databases are based on the relational model, an intuitive, straightforward way of representing data in tables. In a relational database, each table (also called a relation) consists of rows and columns, where each row represents a unique record and each column represents a specific attribute of the record.
The key features of relational databases include:

- **Tables**: Data is organized into tables, which consist of rows and columns. Each table represents a specific entity or concept, and each row represents a unique instance of that entity.
- **Relationships**: Tables can be related to one another through the use of keys. A
- **primary key** is a unique identifier for each record in a table, while a **foreign key** is a field in one table that refers to the primary key in another table. This allows for the establishment of relationships between different tables.
- **SQL**: Relational databases use SQL (Structured Query Language) as the standard language for querying and managing the data. SQL provides a powerful and flexible way to interact with the database, allowing users to perform various operations such as querying, inserting, updating, and deleting data.
- **Data Integrity**: Relational databases enforce data integrity through the use of constraints, such as unique constraints, not null constraints, and referential integrity constraints. This ensures that the data remains accurate and consistent

# what is a database table?

- A table is a collection of related data entries, and it consists of columns and rows.
- A column holds specific information about every record in the table.
- A record (or row) is each individual entry that exists in a table.
- Look at a selection from the Northwind "Customers" table:

| CustomerID | CustomerName                       | ContactName       | Address                     | City         | PostalCode | Country |
|------------|------------------------------------|-------------------|-----------------------------|--------------|------------|---------|
| 1          | Alfreds Futterkiste                | Maria Anders      | Obere Str. 57               | Berlin       | 12209      | Germany |
| 2          | Ana Trujillo Emparedados y helados | Ana Trujillo      | Avda. de la Constitución 2222| México D.F. | 05021      | Mexico  |
| 3          | Antonio Moreno Taquería            | Antonio Moreno    | Mataderos 2312              | México D.F. | 05023      | Mexico  |
| 4          | Around the Horn                    | Thomas Hardy      | 120 Hanover Sq.             | London       | WA1 1DP    | UK      |
| 5          | Berglunds snabbköp                 | Christina Berglund| Berguvsvägen 8              | Luleå        | S-958 22   | Sweden  |

The columns in the "Customers" table above are: CustomerID, CustomerName, ContactName, Address, City, PostalCode and Country. The table has 5 records (rows).

## Relational database table

A relational database defines database relationships in the form of tables. The tables are related to each other - based on data common to each.

Look at the following three tables "Customers", "Orders", and "Shippers" from the Northwind database:

Customers Table

| CustomerID | CustomerName                       | ContactName        | Address                      | City        | PostalCode | Country |
|------------|------------------------------------|--------------------|------------------------------|-------------|------------|---------|
| 1          | Alfreds Futterkiste                | Maria Anders       | Obere Str. 57                | Berlin      | 12209      | Germany |
| 2          | Ana Trujillo Emparedados y helados | Ana Trujillo       | Avda. de la Constitución 2222| México D.F. | 05021      | Mexico  |
| 3          | Antonio Moreno Taquería            | Antonio Moreno     | Mataderos 2312               | México D.F. | 05023      | Mexico  |
| 4          | Around the Horn                    | Thomas Hardy       | 120 Hanover Sq.              | London      | WA1 1DP    | UK      |
| 5          | Berglunds snabbköp                 | Christina Berglund | Berguvsvägen 8               | Luleå       | S-958 22   | Sweden  |

The relationship between the "Customers" table and the "Orders" table is the CustomerID column:

Orders Table

| OrderID | CustomerID | EmployeeID | OrderDate  | ShipperID |
|---------|------------|------------|------------|-----------|
| 10248   | 1          | 5          | 1996-07-04 | 3         |
| 10249   | 2          | 6          | 1996-07-05 | 1         |
| 10250   | 3          | 4          | 1996-07-08 | 2         |
| 10251   | 4          | 3          | 1996-07-08 | 1         |
| 10252   | 5          | 4          | 1996-07-09 | 2         |

The relationship between the "Orders" table and the "Shippers" table is the ShipperID column:

Shippers Table

| ShipperID | ShipperName        | Phone          |
|-----------|--------------------|----------------|
| 1         | Speedy Express     | (503) 555-9831 |
| 2         | United Package     | (503) 555-3199 |
| 3         | Federal Shipping   | (503) 555-9931 |

that is all in a nutshell.
There is so much information and to learn about relational databases and SQL that it would be impossible to cover it all here.
This information can be found and learn at your leisure at a later time.
when i started out this was all the info needed to at least get me started.

## Sql Basics

SQL (Structured Query Language) is a standard language for managing and manipulating relational databases. It provides a way to interact with the data stored in a database, allowing you to perform various operations such as querying, inserting, updating, and deleting data.
Some key features of SQL include:

 - Enables Database Communication: SQL is the programming language that helps design, assess, maintain, protect, and maintain SQL databases.
 - Declarative Language: SQL utilizes a declarative programming approach by describing what a program does without controlling its workflow.
 - Wide range of usage: SQL is a popular programming language and adapted by almost all Relational Database Management Systems(RDMS) like MySQL, MS Access, Oracle, Postgres, and SQL Server.
 - Easy syntax: SQL has a straightforward syntax and can be easy to learn and understand, even without any prior programming knowledge.
 - Wide range of commands: SQL supports DQL (Data Query Language) commands like SELECT; DDL (Data Definition Language) commands like CREATE, DROP; DCL (Data Control Language) commands like GRANT, REVOKE; DML (Data Manipulation Language) commands like INSERT, UPDATE, DELETE; and TCL (Transaction Control Language) commands like COMMIT, ROLLBACK.
 - Scalability and flexibility: As stated earlier, SQL can help add new tables, edit new tables, and delete old tables that are no longer in use. Hence, it can scale up/down to accommodate datasets according to business needs.
 - Integrations with other non-SQL databases: SQL uses a third piece of middleware called an ODBC driver to connect to non-SQL databases like Oracle and Salesforce.


Below website is the best resource to learn "SQL" from scratch for free. this will be your homework for the next week.
[SQLBolt](https://sqlbolt.com/)



## Using SQLite with Python and our example

The SQLite database is available in Python, and according to the SQLite home page, it’s used more than all other database systems combined. 
It offers a full-featured relational database management system (RDBMS) that works with a single file to maintain all the database functionality.

It also has the advantage of not requiring a separate database server to function. The database file format is cross-platform and accessible to any programming language that supports SQLite.

when we look at our accompanying csv file. can you determine a table name. and column names?
The table name could be "ip_addresses" and the column names could be:
- ip_address
- hostname
- department
- assigned_date
- notes
- id (we will add this one ourself as a **primary key**)

**what is a primary key actually?**
A primary key is a unique identifier for each record in a database table. It ensures that each record can be uniquely identified and accessed. 
A primary key must contain unique values and cannot contain NULL values. It is used to establish and enforce entity integrity within the table.

**what is a null value?**
A NULL value in a database represents the absence of a value or an unknown value. It is different from an empty string or a zero value, as those are considered actual values. 
NULL indicates that the value for a particular field is missing or not applicable.

lets start up sqlite on our cli!!
```bash
sqlite3 ip_manager_cli_test.db
```

you will get something like this:

```bash
SQLite version 3.51.0 2025-06-12 13:14:41
Enter ".help" for usage hints.
sqlite> 
```

and now we can learn to create a table in our database.

```sql
CREATE TABLE ip_addresses (
    id INTEGER PRIMARY KEY,
    ip_address TEXT NOT NULL,
    hostname TEXT NOT NULL,
    department TEXT,
    assigned_date TEXT,
    notes TEXT
);
```
you can learn about creating tables and there options here: [SQLbolt](https://sqlbolt.com/lesson/creating_tables)
lets explain:

i start with the **CREATE TABLE** command. and it expects a name for the table. in our case "ip_addresses".
then we open a parenthesis and start defining the columns of our table.
the first column is "id" and it is of type INTEGER. and it is also the **PRIMARY KEY** of the table.
the next column is "ip_address" and it is of type TEXT. and it is also defined as **NOT NULL**. meaning it must have a value.
the next column is "hostname" and it is also of type TEXT and defined as **NOT NULL**.
the next column is "department" and it is of type TEXT. but it is not defined as **NOT NULL**. meaning it can have a null value.
the next column is "assigned_date" and it is of type TEXT. but it is not defined as **NOT NULL**. meaning it can have a null value.
the last column is "notes" and it is of type TEXT. but it is not defined as **NOT NULL**. meaning it can have a null value.
finally we close the parenthesis and end the command with a semicolon.

now we can check if our table was created successfully with the following command:

```sql
.tables
```
and we see our table in there.
but there is no data now. we can check that with the following command:

```sql
SELECT * FROM ip_addresses;
```
and we see nothing. because there is no data in the table yet.

lets make some data entries with the following command:

```sql
INSERT INTO ip_addresses (ip_address, hostname, department, assigned_date, notes) VALUES
('192.168.1.10', 'printer01', 'HR', '2023-01-15', 'Main office printer'),
('192.168.1.20', 'laptop-alice', 'Marketing', '2023-02-05', 'Alice''s laptop'),
('192.168.1.30', 'desktop-bob', 'Engineering', '2023-03-10', 'Bob''s workstation'),
('192.168.1.40', 'server-file01', 'IT', '2023-01-20', 'File server'),
('192.168.1.50', 'laptop-carol', 'Sales', '2023-02-12', 'Carol''s laptop'),
('192.168.1.60', 'desktop-dave', 'Accounting', '2023-03-15', 'Dave''s workstation'),
('192.168.1.100', 'server-db01', 'IT', '2023-01-10', 'Database server'),
('192.168.1.101', 'printer02', 'Marketing', '2023-02-18', 'Marketing printer'),
('192.168.1.102', 'ap-conference', 'IT', '2023-01-25', 'Conference room access point'),
('192.168.1.200', 'router-main', 'IT', '2023-01-05', 'Main office router');
```
we can exit sqlite with the following command:
```sql
.quit
``` 

now that we have some information in our database table. we can play around with it. by using what we learned on the sqlbolt website.
[SQLbolt](https://sqlbolt.com/)


lets take a step back and look ar out csv again.
we could make other tables from this data. so to group our data better together.
can you see any other tables we could make from this data?
we could make a table for departments. a table for devices. and a table for devices <-> users.

we call these types relations.

# one-to-many relationships:
A one-to-many relationship occurs when a record in one table can be associated with multiple records in another table. 
For example, in our IP address manager, one department can have many devices assigned to it.

#### Example:

A common scenario: Departments → Devices

One department can have many devices.

##### Department Table

| dept_id | name        |
| ------- | ----------- |
| 1       | HR          |
| 2       | Marketing   |
| 3       | Engineering |
| 4       | IT          |
| 5       | Sales       |
| 6       | Accounting  |

##### Device Table

| device_id | ip_address   | hostname     | assigned_date | dept_id | notes               |
| --------- | ------------ | ------------ | ------------- | ------- | ------------------- |
| 1         | 192.168.1.10 | printer01    | 2023-01-15    | 1       | Main office printer |
| 2         | 192.168.1.20 | laptop-alice | 2023-02-05    | 2       | Alice's laptop      |


Relationship: Department.dept_id → Device.dept_id (One-to-Many)

# many-to-many relationships:
A many-to-many relationship occurs when multiple records in one table can be associated with multiple records in another table.
For example, in our IP address manager, a device can be assigned to multiple users, and a user can have multiple devices assigned to them.

#### Example:
A user can use multiple devices, and a device could be shared among multiple users.

We need a junction table.

##### User Table 

| user_id | name  |
| ------- | ----- |
| 1       | Alice |
| 2       | Bob   |
| 3       | Carol |
| 4       | Dave  |

| device_id | ip_address   | hostname     | assigned_date | dept_id | notes               |
| --------- | ------------ | ------------ | ------------- | ------- | ------------------- |
| 1         | 192.168.1.10 | printer01    | 2023-01-15    | 1       | Main office printer |
| 2         | 192.168.1.20 | laptop-alice | 2023-02-05    | 2       | Alice's laptop      |

and then we need the "junction table" to connect them.

##### UserDevice Table (junction)

| user_id | device_id |                           |
| ------- | --------- | ------------------------- |
| 1       | 2         | → Alice uses laptop-alice |
| 2       | 3         | → Bob uses desktop-bob    |
| 3       | 5         | → Carol uses laptop-carol |
| 4       | 6         | → Dave uses desktop-dave  |


note that is a very simplictic way of looking at it. but it is enough for now.
you can study for 1000s of hours on relational database design and still not know everything about it.

lets work with my simple yet not perfect example.

## SQL Schema for above example

note: pasting this into the sqlite interface probably wont work because of the comments.
so save below into a file: ip_manager_schema_and_fixtures.sql

then start sqlite with a new database file and import the sql file like this:

```bash
sqlite3 ip_manager_full_example.db < ip_manager_schema_and_fixtures.sql
```


```sql
-- ===========================
-- Drop old tables (if exist)
-- ===========================
DROP TABLE IF EXISTS UserDevice;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Device;
DROP TABLE IF EXISTS Department;

-- ===========================
-- Department Table
-- ===========================
CREATE TABLE Department (
    dept_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO Department (dept_id, name) VALUES
(1, 'HR'),
(2, 'Marketing'),
(3, 'Engineering'),
(4, 'IT'),
(5, 'Sales'),
(6, 'Accounting');

-- ===========================
-- Device Table
-- ===========================
CREATE TABLE Device (
    device_id INTEGER PRIMARY KEY,
    ip_address TEXT,
    hostname TEXT,
    assigned_date TEXT,
    notes TEXT,
    dept_id INTEGER,
    FOREIGN KEY(dept_id) REFERENCES Department(dept_id)
);

INSERT INTO Device (device_id, ip_address, hostname, assigned_date, notes, dept_id) VALUES
(1,'192.168.1.10','printer01','2023-01-15','Main office printer',1),
(2,'192.168.1.20','laptop-alice','2023-02-05','Alice''s laptop',2),
(3,'192.168.1.30','desktop-bob','2023-03-10','Bob''s workstation',3),
(4,'192.168.1.40','server-file01','2023-01-20','File server',4),
(5,'192.168.1.50','laptop-carol','2023-02-12','Carol''s laptop',5),
(6,'192.168.1.60','desktop-dave','2023-03-15','Dave''s workstation',6),
(7,'192.168.1.100','server-db01','2023-01-10','Database server',4),
(8,'192.168.1.101','printer02','2023-02-18','Marketing printer',2),
(9,'192.168.1.102','ap-conference','2023-01-25','Conference room access point',4),
(10,'192.168.1.200','router-main','2023-01-05','Main office router',4);

-- ===========================
-- Users Table
-- ===========================
CREATE TABLE User (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO User (user_id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Carol'),
(4, 'Dave');

-- ===========================
-- UserDevice (Junction Table)
-- ===========================
CREATE TABLE UserDevice (
    user_id INTEGER,
    device_id INTEGER,
    PRIMARY KEY (user_id, device_id),
    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY(device_id) REFERENCES Device(device_id)
);

INSERT INTO UserDevice (user_id, device_id) VALUES
(1, 2),   -- Alice → laptop-alice
(2, 3),   -- Bob → desktop-bob
(3, 5),   -- Carol → laptop-carol
(4, 6),   -- Dave → desktop-dave
(1, 1),   -- Alice → printer01
(2, 1);   -- Bob also uses printer01
```


## Examples of querying this data

```sql
#1. Show all devices
         
SELECT * FROM Device;

#2. Show all departments
         
SELECT * FROM Department;

#3. Show all users
         
SELECT * FROM User;


#📊 One-to-Many Examples (Department → Device)
                                     
#4. Devices in the IT department

SELECT d.hostname, d.ip_address
FROM Device d
JOIN Department dep ON d.dept_id = dep.dept_id
WHERE dep.name = 'IT';

#5. Count devices per department
          
SELECT dep.name AS department, COUNT(d.device_id) AS device_count
FROM Department dep
LEFT JOIN Device d ON dep.dept_id = d.dept_id
GROUP BY dep.name;

#6. Devices assigned after February 1, 2023
            
SELECT hostname, assigned_date
FROM Device
WHERE assigned_date > '2023-02-01';

#🔀 Many-to-Many Examples (Users ↔ Devices)
                                 
#7. Devices used by Alice

SELECT u.name AS user, d.hostname, d.ip_address
FROM User u
JOIN UserDevice ud ON u.user_id = ud.user_id
JOIN Device d ON ud.device_id = d.device_id
WHERE u.name = 'Alice';

#8. Who uses printer01?
        
SELECT u.name
FROM User u
JOIN UserDevice ud ON u.user_id = ud.user_id
JOIN Device d ON ud.device_id = d.device_id
WHERE d.hostname = 'printer01';

#9. All users and their devices
        
SELECT u.name AS user, d.hostname AS device
FROM User u
JOIN UserDevice ud ON u.user_id = ud.user_id
JOIN Device d ON ud.device_id = d.device_id
ORDER BY u.name;

#10. Which devices are shared by more than one user?
           
SELECT d.hostname, COUNT(ud.user_id) AS user_count
FROM Device d
JOIN UserDevice ud ON d.device_id = ud.device_id
GROUP BY d.device_id
HAVING COUNT(ud.user_id) > 1;

#🧩 More Advanced
    
#11. List each department with the users who use its devices

SELECT dep.name AS department, u.name AS user, d.hostname AS device
FROM Department dep
JOIN Device d ON dep.dept_id = d.dept_id
JOIN UserDevice ud ON d.device_id = ud.device_id
JOIN User u ON ud.user_id = u.user_id
ORDER BY dep.name, u.name;

#12. Departments with no devices
                 
SELECT dep.name
FROM Department dep
LEFT JOIN Device d ON dep.dept_id = d.dept_id
WHERE d.device_id IS NULL;

```


Below not working yet. is for later.


we will use the following python script to create a database and a table in it. and then we will populate the table with data from our csv file.

```python
import sqlite3
import csv
from time import sleep  
from sqlite3 import Error
from typing import List, Dict, Any
from contextlib import closing
from pathlib import Path
DB_FILE = "ip_manager.db"
CSV_FILE = "ip_manager.csv"
TABLE_NAME = "ip_addresses"

def create_connection(db_file: str) -> sqlite3.Connection:
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(e)
    return conn

def create_table(conn: sqlite3.Connection, create_table_sql: str) -> None:
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement       
    :return:
    """
    try:
        with closing(conn.cursor()) as c:
            c.execute(create_table_sql)
            print(f"Table created or already exists.")
    except Error as e:
        print(e)
        
def insert_entry(conn: sqlite3.Connection, entry: Dict[str, Any]) -> int:
    """ Create a new entry into the ip_addresses table
    :param conn:
    :param entry:
    :return: entry id
    """
    sql = ''' INSERT INTO ip_addresses(ip_address,hostname,department,assigned_date,notes
                ) VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (entry['ip_address'], entry['hostname'], entry['department'],
                        entry['assigned_date'], entry['notes']))
    conn.commit()
    return cur.lastrowid

def load_csv_data(filename: str) -> List[Dict[str, Any]]:
    data = []
    with open(filename, newline='') as csvfile:
        content = csv.DictReader(csvfile)
        for row in content:
            data.append(row)
    return data

def main():
    database = DB_FILE
    sql_create_ip_addresses_table = f""" CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                                        id integer PRIMARY KEY,
                                        ip_address text NOT NULL,
                                        hostname text NOT NULL,
                                        department text,
                                        assigned_date text,
                                        notes text
                                    ); """
    # create a database connection
    conn = create_connection(database)
    # create tables
    if conn is not None:
        # create ip_addresses table
        create_table(conn, sql_create_ip_addresses_table)
        # load data from csv file
        csv_data = load_csv_data(CSV_FILE)
        print(f"Loaded {len(csv_data)} entries from {CSV_FILE}")
        # insert data into table
        for entry in csv_data:
            entry_id = insert_entry(conn, entry)
            print(f"Inserted entry with id: {entry_id}")
            sleep(0.1)  # simulate some delay
        print("All data inserted.")
    else:
        print("Error! cannot create the database connection.")
if __name__ == '__main__':
    main()
```







import sqlite3

from sqlite3 import Error

def sql_connection():   #Establish a connection
    try:                #Exception handling (try,except,finally)
        conn = sqlite3.connect('student1.db') #Create or Open existing database
        return conn
    except Error:
        print(Error)
print("create student table ")
print("================================================")

def sql_table(conn):  #Sales.db
    cursorObj = conn.cursor() #points to the database Sales.db
    #Create the table in Sales.db
    cursorObj.execute("CREATE TABLE student1 (student_id n(5), name char(30), city char(35));")
    # Insert records
    cursorObj.executescript("""
   INSERT INTO student1 VALUES(1001,'varsha', 'karnataka');
   INSERT INTO student1 VALUES(1002,'nayaan', 'karnataka');
   INSERT INTO student1 VALUES(1003,'urmila', 'andra');
   INSERT INTO student1 VALUES(1004,'lakshmi', 'andra');
   INSERT INTO student1 VALUES(1005,'priya', 'tamilnadu');

   """)
    conn.commit() #STORE THE DATA PERMANENTLY
    cursorObj.execute("SELECT * FROM student1")
    #cursorObj.execute("SELECT name,city FROM salesman WHERE salesman_id >= 5001 and salesman_id <=5004") # * -> all columns ->WHERE CLAUSE-SELECTED ROWS
    rows = cursorObj.fetchall()  # rows-> all the records in the salesman table
    print("Agent details:")
    for row in rows:
        print(row)

sqllite_conn = sql_connection() #Sales.db
sql_table(sqllite_conn) #Sales.db
if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")
print("======================================================\n")
print("insert operation ")
print("======================================================\n")

def sql_connection():
    try:
        conn = sqlite3.connect('student1.db')
        return conn
    except Error:
        print(Error)
def sql_table(conn):
    cursorObj = conn.cursor()

    cursor = cursorObj.execute('select * from student1;')
    print(len(cursor.fetchall()))
    # Insert records
    cursorObj.executescript("""
    INSERT INTO student1 VALUES(1006,'James Hoog', 'New York');
    INSERT INTO student1 VALUES(1007,'Nail Knite', 'Paris');
    INSERT INTO student1 VALUES(1008,'Pit Alex', 'London');
    INSERT INTO student1 VALUES(1009,'Mc Lyon', 'Paris');
    INSERT INTO student1 VALUES(1010,'Paul Adam', 'Rome');
    """)
    conn.commit()
    print("======================================================\n")
    print("\nNumber of records after inserting rows:")
    print("======================================================\n")
    cursor = cursorObj.execute('select * from student1;')
    print(len(cursor.fetchall()))
sqllite_conn = sql_connection()
sql_table(sqllite_conn)

if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")
print("======================================================\n")
print("update operation")
print("======================================================\n")
def sql_connection():
    try:
      conn = sqlite3.connect('student1.db')
      return conn
    except Error:
      print(Error)
def sql_table(conn):
    cursorObj = conn.cursor()  #Sales.db
    #Current records in salesman table
    cursorObj.execute("SELECT * FROM student1")
    rows = cursorObj.fetchall()
    print("before update details:")
    print("======================================================\n")
    for row in rows:
        print(row)
    print("\nUpdate student_id 1001 to 1003 where id is 1005:")
    sql_update_query = """Update student1 set student_id = 1001 where student_id =1003"""
    cursorObj.execute(sql_update_query)
    conn.commit()
    print("======================================================\n")
    print("Record Updated successfully ")
    print("======================================================\n")
    cursorObj.execute("SELECT * FROM student1")
    rows = cursorObj.fetchall()
    print("\nAfter updating student  details:")
    print("======================================================\n")
    for row in rows:
        print(row)
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
  sqllite_conn.close()
  print("\nThe SQLite connection is closed.")
print("======================================================\n")
print("delete operation")
print("======================================================\n")
#print("delete operation ")
def sql_connection():
    try:
        conn=sqlite3.connect('student1.db')
        return conn
    except Error:
        print(Error)
def sql_table(conn):
    cursorObj=conn.cursor()
    cursorObj.execute("SELECT * FROM student1")
    rows=cursorObj.fetchall()
    print("details:")
    for x in rows:
        print(x)
    print("\n Delete student_id 105:")
    student_id=1005
    cursorObj.execute("""
    DELETE FROM student1 
    WHERE student_id=?
    """,(student_id,))
    conn.commit()
    cursorObj.execute("select * from student1")
    rows =cursorObj.fetchall()
    print("\n after delete details:")
    for x in rows:
        print(x)
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
  sqllite_conn.close()
  print("\nThe SQLite connection is closed.")
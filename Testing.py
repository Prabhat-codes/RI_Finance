import psycopg2
#Establishing the connection
conn = psycopg2.connect(database="mydb", user='prince', password='password',host='127.0.0.1', port= '5432')
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Creating table as per requirement
sql ='''DROP TABLE IF EXISTS EMPLOYEE;
        CREATE TABLE EMPLOYEE(
            FIRST_NAME CHAR(20) NOT NULL,
            LAST_NAME CHAR(20),
            AGE INT,
            SEX CHAR(1),
            INCOME FLOAT
            )    
     '''
cursor.execute(sql)
print("Table created successfully........")

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Ramya', 'Rama priya', 27, 'F', 9000)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Vinay', 'Battacharya', 20, 'M', 6000)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Sharukh', 'Sheik', 25, 'M', 8300)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Sarmista', 'Sharma', 26, 'F', 10000)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Tripthi', 'Mishra', 24, 'F', 6000)''')

cursor.execute('''SELECT * from EMPLOYEE''')
# #Fetching 1st row from the table
# result = cursor.fetchone()
# print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Closing the connection
conn.close()
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
#Closing the connection
conn.close()
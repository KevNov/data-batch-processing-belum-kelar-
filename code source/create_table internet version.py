import psycopg2

#connection to postgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=576831")

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping CITIZEN table if already exists.
cursor.execute("DROP TABLE IF EXISTS CITIZEN_DATA")

#Creating table as per requirement
sql ='''CREATE TABLE CITIZEN_DATA(
   Index serial primary key,
   User_id CHAR(20),
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20) NOT NULL,
   SEX CHAR(10),
   Email CHAR (30),
   Phone varchar(30),
   Date_of_birth date,
   Job_Title CHAR(30)
)'''

cursor.execute(sql)
print("Table created successfully........")
conn.commit()

#Closing the connection
conn.close()
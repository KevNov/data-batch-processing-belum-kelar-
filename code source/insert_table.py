import psycopg2
import csv

#connection to postgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=576831")
cur = conn.cursor()

#read csv file table
with open('C:\\Users\\kevnov\\Documents\\Data batch processing\\source data\\dataclean-people-100.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)

#insert table from csv file
with open('C:\\Users\\kevnov\\Documents\\Data batch processing\\source data\\dataclean-people-100.csv','r') as csv_file:
    next(csv_file)
    cur.copy_from(csv_file,'citizen_data',sep=',',columns=('index','user_id','first_name','last_name', 'sex', 'email', 'phone', 'date_of_birth', 'job_title'))
conn.commit()       
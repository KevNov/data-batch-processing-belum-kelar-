import psycopg2
import pandas as pd

#connection to postgresql
try:
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=576831")
    print("connection sucess")
except:
    print("connection failed")

#menggunakan kursor
cur = conn.cursor()
cur.execute("select * from public.anggota")

#menampilkan hasil
one = cur.fetchone()
all = cur.fetchall()
conn.commit()

for i in all:
    print(i)
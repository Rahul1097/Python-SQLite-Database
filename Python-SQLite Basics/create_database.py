import sqlite3

#create database
conn = sqlite3.connect('customer.db')

#create cursor
cur = conn.cursor()

#create a table
cur.execute(""" CREATE TABLE customers (
                first_name text,
                last_name text,
                email text
            )""")

#commit changes to database
conn.commit()

#close the connection
conn.close()


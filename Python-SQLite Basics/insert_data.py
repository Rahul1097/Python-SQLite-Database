import sqlite3

#create database
conn = sqlite3.connect('customer.db')

#create cursor
cur = conn.cursor()

#insert one record to database
cur.execute("INSERT INTO customers VALUES ('Robert','Kelly','Robert.Kelly@gmail.com')")


# insert many records at one time into database
many_customers = [
                  ('Renee','Brown','renee.brown@gmail.com'),
                  ('Akshay','Chavan','akshay1234@yahoo.com'),
                  ('Ramesh','Gupta','ramesh.gupta67@gmail.com')
                  ]

cur.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)

#commit changes to database
conn.commit()

#close the connection
conn.close()


import sqlite3

#create database
conn = sqlite3.connect('customer.db')

#create cursor
cur = conn.cursor()

#update records
#cur.execute("UPDATE customers SET first_name = 'Bob' WHERE rowid = 2 ")

#delete records
cur.execute("DELETE FROM customers WHERE rowid = 2")

conn.commit()
#query the database
cur.execute("SELECT rowid,* FROM customers")
# print(cur.fetchone())
#print(cur.fetchmany(2))

records = cur.fetchall()
print(records)


# #formating the data
# print("FIRST NAME \t LASTNAME \t EMAIL ADDRESS")
# print("---------------------------------------------------------")
# for record in records:
#     print(record[0] + "\t\t" +record[1] + "\t\t" + record[2])

#close the connection
conn.close()


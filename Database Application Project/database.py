import sqlite3

def create_table(conn,cur):

    cur.execute(""" CREATE TABLE books(
                name TEXT,
                author TEXT,
                price REAL
            )""")

    commit_changes(conn)
    print("Books table created!!")

def insert_one_record(conn,cur):
    cur.execute("INSERT INTO books VALUES ('ABC','Robert','250.50')")
    commit_changes(conn)


def insert_many_records(conn,cur):
    many_books = [
                  ('XYZ','Mary','556.36'),
                  ('JKJ','Yogesh','854.21'),
                  ('NKN','Gupta','780.26')
                  ]

    cur.executemany("INSERT INTO books VALUES (?,?,?)",many_books)
    commit_changes(conn)

def update_record(conn,cur):
    cur.execute("UPDATE books SET price = '256.12' WHERE rowid = 2 ")
    commit_changes(conn)

def delete_record(conn,cur):
    cur.execute("DELETE FROM books WHERE rowid = 2")
    commit_changes(conn)

def drop_table(conn,cur):
    cur.execute("DROP TABLE books")
    commit_changes(conn)

def commit_changes(conn):
    conn.commit()

def show_database_records(conn,cur):
    cur.execute("SELECT * FROM books")
    records = cur.fetchall()
    print("Book Name \t Author \t Price")
    print("---------------------------------------------------------")
    for record in records:
        print(record[0] + "\t\t" +record[1] + "\t\t" + str(record[2]))

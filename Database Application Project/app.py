import database
import sqlite3

database_name = 'books.db'

books_map = {
    '1':database.create_table,
    '2':database.show_database_records,
    '3':database.insert_one_record,
    '4':database.insert_many_records,
    '5':database.update_record,
    '6':database.delete_record,
    '7':database.drop_table
}

def show_menu():
    while True:
        menu = '''Enter the number for the operation you want to perform on database:
                1.Create Database Table
                2.Show all Database Records
                3.Insert One Record into Database
                4.Insert Many Record into Database
                5.Update Data in Database
                6.Delete Record in Database
                7.Drop Table from Database
        '''
        user_input = (input(menu))

        try:
            conn = sqlite3.connect(database_name)
            print("Database Connection Established!!")
        except sqlite3.Error as error:
            print("Error while connecting to sqlite Database", error)
            exit()

        cur = conn.cursor()

        selection_func = books_map[user_input]

        selection_func(conn,cur)

show_menu()
        
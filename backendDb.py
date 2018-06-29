#  AUTHOR:  Michael O'Brien
#  CREATED:  25 June 2018
#  UPDATED:  25 June 2018
#  DESCRIPTION:  Backend DB for Bookstore app


#  Import libraries need for DB
import sqlite3


#  Function  to create the database and tables and variable declaration for connection and cursor
def create_table():
    dbConnection = sqlite3.connect('bookstore.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
    dbConnection.commit()
    dbConnection.close()


def insert_data(title, author, year, isbn):
    dbConnection = sqlite3.connect('bookstore.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('INSERT INTO books VALUES (NULL, ?, ?, ?, ?)', (title, author, year, isbn))
    dbConnection.commit()
    dbConnection.close()


def view_data():
    dbConnection = sqlite3.connect('bookstore.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('SELECT * FROM books')
    rows = dbCursorObject.fetchall()
    dbConnection.close()
    return rows


def search_data(title = "", author = "", year = "", isbn = ""):
    dbConnection = sqlite3.connect('bookstore.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?', (title, author, year, isbn))
    rows = dbCursorObject.fetchall()
    dbConnection.close()
    return rows


def delete_data(id):
    dbConnection = sqlite3.connect('bookstore.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('DELETE FROM books WHERE id = ?', (id,))  #NOTE:  Comma is needed when you are passing a single parameter
    dbConnection.commit()
    dbConnection.close()


def update_data(id, title, author, year, isbn):
    dbConnection = sqlite3.connect('bookstore.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?', (title, author, year, isbn, id))
    dbConnection.commit()
    dbConnection.close()


create_table()
#insert_data('A Reckless Witch', 'Debora Geary', 2012, 152660)
#delete_data(4)
#update_data(4, 'A Nomadic Witch', 'Debora Geary', 2012, 9112012 )
#print(view_data())
#print(search_data(title = 'A Modern Witch'))

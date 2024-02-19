from .database_connection import DatabaseConnection
CONNECTION = 'Databases/FileDatabase/data.db'

def create_book_table():
    with DatabaseConnection(CONNECTION) as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(title text primary key, author text, read integer)')

def add_book(title,author)-> str:
    with DatabaseConnection(CONNECTION) as connection:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO books VALUES(?,?,0)',(title,author))
    print('Book has been added')

def get_all_books()->None:
    with DatabaseConnection(CONNECTION) as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM books')
        books = [{'title':row[0],'author':row[1],'read':row[2],} for row in cursor.fetchall()]
    return books

def mark_as_read(title)->str:
    with DatabaseConnection(CONNECTION) as connection:
        cursor = connection.cursor()
        cursor.execute(f'UPDATE books SET read=1 WHERE title=?',(title,))
    print('Book has been marked')

def delete_book(title) ->str:
    with DatabaseConnection(CONNECTION) as connection:
        cursor = connection.cursor()
        cursor.execute(f'DELETE FROM books WHERE title=?',(title,))
    print('operation finished')
from utils import database

MENU_CHOICE = """
Enter:
-'a' to add new book
-'l' to list all books
-'r' to mark as read
-'d' to delete a book
-'q' to quit
"""

def menu():
    database.create_book_table()
    user_input =input(MENU_CHOICE)
    while user_input!='q':
        if user_input in operations:
            operation = operations[user_input]
            operation()
        else:
            print('Wrong command')
        user_input=input(MENU_CHOICE)


def add_book():
    title = input('Title of the book: ')
    author = input('Author of the book')
    print(database.add_book(title,author))

def list_books():
    books = database.get_all_books()
    for book in books:
        print(book)

def mark_as_read():
    title = input ('Enter the title of book you want to mark as read: ')
    print(database.mark_as_read(title))

def delete_book():
    title = input ('Enter the title of book you want to delete: ')
    print(database.delete_book(title))

operations = {
    'a':add_book,
    'l':list_books,
    'r':mark_as_read,
    'd':delete_book,
}

menu()
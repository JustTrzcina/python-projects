import os
DATA_FOLDER = 'Databases/FileDatabase/books.csv'

def create_book_table():
    with open (DATA_FOLDER,'w'):
        pass

def add_book(title,author)-> str:
    with open(DATA_FOLDER,'a') as books:
        books.writelines(f'{title},{author},0\n')
    return 'Book has been added'

def get_all_books()->None:
    with open(DATA_FOLDER,'r') as books:
        books_data = [book.strip().split(',') for book in books.readlines()]
    return [{'title':book[0],'author':book[1],'read':book[2]}
                for book in books_data]

def mark_as_read(title)->str:
    books = get_all_books()
    for book in books:
        if book['title'] == title:
            book['read']='1'
            break
    _post_all_books(books)
    return 'Book has been marked'

def _post_all_books(books):
    result = [(",".join(book.values())+"\n") for book in books]
    with open(DATA_FOLDER,'w') as books:
        books.writelines(result)

def delete_book(title) ->str:
    books = get_all_books()
    title=title.lower()
    book_index = next((index for index, book in enumerate(books)
                        if (book["title"]).lower() == title), None)
    print(book_index)
    if book_index!=None:
        del books[book_index]
    _post_all_books(books)
    return 'operation finished'
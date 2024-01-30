import logging
from book_scraper import books

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''
Enter one of the follwowing

-'b' to look at the top 5 books
-'c' to look at the cheapest books
-'n' to get the next book on the catalogue
-'q' to exit 
'''

book_generator = (book for book in books)

def menu():
    user_choice = input(USER_CHOICE)
    while user_choice!='q':
        if user_choice in menu_funcions:
            choice = menu_funcions[user_choice]
            choice()
        else:
            print('No such command, try again.')
        user_choice = input(USER_CHOICE)
    logger.debug('Terminating file')
def print_best_books():
    logger.info('Printing best books by rating')
    best_books = sorted(books, key=lambda x: x.rating,reverse=True)[:5]
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info('Printing best books by price asc')
    print_cheapest_books = sorted(books, key=lambda x: x.price)[:5]
    for book in print_cheapest_books:
        print(book)

def print_next_book():
    logger.info('Printing next book')
    print(next(book_generator))

menu_funcions={
    'b':print_best_books,
    'c':print_cheapest_books,
    'n':print_next_book,
}

menu()
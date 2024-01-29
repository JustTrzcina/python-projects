import requests
from pages.books_page import BooksPage

page = requests.get('https://books.toscrape.com/')
page = BooksPage(page.content)

for entry in page.books:
    print(entry)
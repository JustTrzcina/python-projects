from bs4 import BeautifulSoup

from locators.book_page_locators import BookPageLocators
from parsers.book import BookParser

class BooksPage:
    def __init__(self,page):
        self.soup = BeautifulSoup(page,'html.parser')

    @property
    def books(self):
        locator = BookPageLocators.BOOKS
        books = self.soup.select(locator)
        return [BookParser(e) for e in books]
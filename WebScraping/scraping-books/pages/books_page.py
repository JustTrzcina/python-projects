from bs4 import BeautifulSoup
import re
import logging
from locators.book_page_locators import BookPageLocators
from parsers.book import BookParser

logger = logging.getLogger('scraping.books_page')

class BooksPage:
    def __init__(self,page):
        logger.debug('Parsing page content...')
        self.soup = BeautifulSoup(page,'html.parser')

    @property
    def books(self):
        locator = BookPageLocators.BOOKS
        logger.debug(f'Finding books using `{BookPageLocators.BOOKS}`.')
        books = self.soup.select(locator)
        return [BookParser(e) for e in books]
    
    @property
    def pages(self):
        logger.debug('Searching for number of catalogues...')
        content = self.soup.select_one(BookPageLocators.PAGER).string
        logger.info(f'Found available pages: `{content}`')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern,content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted `{pages}` pages.')

        return pages
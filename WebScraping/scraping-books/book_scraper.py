import requests
import logging
from pages.books_page import BooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.INFO)

logger = logging.getLogger('scraping')
logger.info('Loading books...')

page = requests.get(f'https://books.toscrape.com/catalogue/page-1.html')
page = BooksPage(page.content)
books= page.books

for page_num in range(1,5):
    page = requests.get(f'https://books.toscrape.com/catalogue/page-{page_num+1}.html')
    page = BooksPage(page.content)
    books.extend(page.books)
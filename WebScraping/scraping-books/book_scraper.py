import requests
import logging
import aiohttp
import asyncio
import time
from pages.books_page import BooksPage


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.INFO)

logger = logging.getLogger('scraping')
logger.info('Loading books...')

page = requests.get(f'https://books.toscrape.com/catalogue/page-1.html')
page = BooksPage(page.content)

loop = asyncio.new_event_loop()

books= page.books

async def fetch_page(session, url):
    page_start = time.time()
    async with session.get(url) as response:
        print(f'Took {time.time()-page_start}')
        return await response.text()
        
async def get_multiple_pages(loop,*urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))       
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

urls = [f'https://books.toscrape.com/catalogue/page-{page_num+1}.html' for page_num in range (1,page.pages)]
start=time.time()
pages=loop.run_until_complete(get_multiple_pages(loop,*urls))
print(f'Took {time.time()-start} seconds')

for page_content in pages:
    page = BooksPage(page_content)
    books.extend(page.books)
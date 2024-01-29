from pages.quotes_page import QuotesPage
import requests

page = requests.get('https://quotes.toscrape.com/')
page = QuotesPage(page.content)

for quote in page.quotes:
    print(quote)
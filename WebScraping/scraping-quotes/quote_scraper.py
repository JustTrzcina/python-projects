from selenium import webdriver
from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:
    author = input("Enter the author's name: ")
    tag = input('Select enter tag:')

    chrome = webdriver.Chrome()
    chrome.get('https://quotes.toscrape.com/search.aspx')
    page = QuotesPage(chrome)
    print(page.search_for_quotes(author,tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print('Unknown error')
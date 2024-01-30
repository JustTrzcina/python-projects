import re
import logging
from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book')

class BookParser:
    def __init__(self,parent) -> None:
        logger.debug(f'New book parsers created.')
        self.parent = parent

    def __repr__(self):
        return f'<Book "{self.title}" for {self.price} with {self.rating} stars.>'

    RATINGS = {
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5
    }

    @property
    def title(self):
        logger.debug('Finding book name...')
        locator=BookLocators.TITLE
        title = self.parent.select_one(locator).attrs['title']
        logger.debug(f'Found `{title}`')
        return title

    @property
    def link(self):
        logger.debug('Finding book link...')
        locator=BookLocators.LINK
        link = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found `{link}` link')

        return link
        
    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE
        item_price = self.parent.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern,item_price)
        price =float(matcher.group(1)) 
        logger.debug(f'Found `{price}` price')
        return price

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r !='star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        logger.debug(f'Found rating of `{rating_number}`')
        return rating_number
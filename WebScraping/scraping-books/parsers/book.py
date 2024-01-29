import re
from locators.book_locators import BookLocators
class BookParser:
    def __init__(self,parent) -> None:
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
        locator=BookLocators.TITLE
        return self.parent.select_one(locator).attrs['title']

    @property
    def link(self):
        locator=BookLocators.LINK
        return self.parent.select_one(locator).attrs['href']
        
    @property
    def price(self):
        locator = BookLocators.PRICE
        item_price = self.parent.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern,item_price)
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = BookLocators.RATING
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r !='star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        return rating_number
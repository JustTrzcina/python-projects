def hundred_numbers():
    i = 0
    while i<100:
        yield i
        i+=1

g = hundred_numbers()
print(next(g))
print(next(g))

class HundredGenerator:
    def __init__(self) -> None:
        self.number = 0

    def __next__(self):
        if self.number<100:
            current = self.number
            self.number+=1
            return current
        else:
            raise StopIteration()
        
    def __iter__(self):
        return self
        
generator = HundredGenerator()

class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1,2,3,4,5]
        self.i=0
    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i +=1
            return current
        else:
            raise StopIteration()  
        
five_gen = FirstFiveIterator()

class AnotherIterable:
    def __init__(self) -> None:
        self.cars=['Fiesta','Focus']

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self,i):
        return self.cars[i]
    
    
##generator comprehension
numbers_gen = (x for x in [1,2,3,4,5])
print(next(numbers_gen))

names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]
start_with_e = filter(lambda x:x.startswith('E'),names)

anoter_start_with_e = (n for n in names if n.startswith('E'))

def custom_filter(func,iterable):
    for i in iterable:
        if func(i):
            yield i

names_lower = map(lambda x:x.lower(),names) 
names_lower = [name.lower() for name in names] #better if you need whole list
names_lower = (name.lower() for name in names) ##better if no list needed

class User:
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password
    
    @classmethod
    def from_dict(cls,data):
        return cls(data['username'], data['password'])
    
users = [
    {"username": "alice", "password": "password123"},
    {"username": "bob", "password": "securepass456"},
    {"username": "charlie", "password": "strongpwd789"},
]

user_objects = [User.from_dict(user) for user in users]
user_objects = map(User.from_dict,users)

user_objects = [User(**data) for data in users]

users_with_locations = [
    {"name": "Alice", "location": "New York"},
    {"name": "Bob", "location": "Los Angeles"},
    {"name": "Charlie", "location": "San Francisco"},
    {"name": "David", "location": "San Francisco"},
    {"name": "Eva", "location": "Miami"},
    {"name": "Frank", "location": "Seattle"},
]

your_location = "San Francisco"
users_nearby = [user for user in users_with_locations if user['name']==your_location]

if any(users_nearby):
    print('You are not alone')

accounts = {
    'checking':1900,
    'savings':5320.45
}

def add_balance(amount,name = 'checking'):
    accounts[name]+=amount
    return accounts[name]

transactions=[
    (-182,'checking'),
    (-234,'checking'),
    (-53,'checking'),
    (182,'savings'),
    (120,'savings'),
    (-182,'checking'),
    (-182,'checking'),
]

for t in transactions:
    add_balance(*t)

from collections import Counter

temperatures = [12.3,14.0,9.0,15.3,10.5,12.0]
temperature_counter = Counter(temperatures)
print(temperature_counter)

from collections import defaultdict

coworkers = [('John','MIT'),('Katie','Oxford'),('Charlie','UMK'),('Katie','Cambrdige')]

places = defaultdict(list)
for coworker, place in coworkers:
    places[coworker].append(place)

print(places)

from collections import OrderedDict

o = OrderedDict()
o['John'] = 6
o['Steve'] = 12
o['Katie'] = 3
print (o)
o.move_to_end('John')
o.move_to_end('Katie', last=False),
print (o)
o.popitem()
print(o)

from collections import namedtuple

account = ('checking',1700.00)
print(account[0])
print(account[1])

Account = namedtuple('Account',['name','balance'])

account = Account('checking',1700.00)
print(account)
print(account.balance)

accountNamedTuple = Account(*account)
print(accountNamedTuple._asdict()['balance'])

from collections import deque

friends = deque(('John','Steve','Katie','Anna'))
friends.append('Charlie')
friends.appendleft('Giorgio')
print(friends)
friends.pop()
friends.popleft()
print(friends)

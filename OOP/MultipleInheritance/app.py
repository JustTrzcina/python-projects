from admin import Admin
from database import Database
from user import User


a = Admin('John','HardPassword',3)
u = User('Drew','HardPassword')

users=[a,u]
print(Database.find(lambda x: x['username'] == 'John'))

for user in users:
    user.save()
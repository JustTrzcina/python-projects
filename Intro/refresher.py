favourite_food = ['steak','pastry']
food_types = ["pasta","pizza",'gnocchi']

requested_food = input('what would you like to eat: ')

if requested_food in favourite_food:
    print("That is your favourite")
elif requested_food in food_types:
    print("You like this one")
else:
    print('Sorry we dont have this one')

is_driving=True

while is_driving:
    print("Driving")
    user_input = input("Are you still driving?")
    is_driving = user_input.lower()=="yes"

for food in favourite_food:
    print(food)

for index in range(6):
    print(index)

students = [
    {"name":"Bob","age":55},
    {"name":"John","age":12},
    {"name":"Steve","age":43},
    {"name":"Marc","age":24}
]

for student in students:
    name = student['name']
    age = student['age']
    print(f"{name} is {age} years old")

#Destructuring
friends = [("John", 35),("Luna", 22),("Katie", 38),("Mark", 29)]
for name, age in friends:
    print(f"{name} is {age} years old")

#Dict iteration
people_dict = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 22,
    "Diana": 28,
    "Eva": 35
}    
for name,age in people_dict.items():
    print(f"{name} is {age} years old")

#For loop with else
status_list = ["Ok", "Ok", "Ok", "Fault", "Ok"]
for status in status_list:
    if status =="Faulty":
        print("Fault detected")
        break
    print (f" This one is {status}")
    print (f" Shipping")
else:
    print("Everything shipped correctly")

for i in range (2,15):
    for j in range (2,i):
        if i%j ==0:
            print(f"{i} equals {j}*{i//j}")
            break
    else:
        print(f"{i} is prime")

#Slicing
colors = ["red","yellow","blue","green","orange"]
print(colors[1:5])

#list comprehension
numbers = [0,1,2,3,4]
doubled_numbers = [number*2 for number in numbers] 
items_count = [f"I have {count} items" for count in doubled_numbers]
print (items_count)
colors_upper = [color.upper() for color in colors]
print(colors_upper)

#conditional comprehension
ages = [22,33,55,66,21]
odds = [age for age in ages if age % 2==1]

friends = ['kate', 'bob', 'Charlie', 'Ian', 'emily']
guests = ['Grace', 'Bob', 'Ian', 'Jack', 'kate', 'Frank']

friends_lower = [friend.lower() for friend in friends]
present_friends = [name.title() for name in guests if name.lower() in friends_lower]
print(present_friends)

#set and dictionary comprehensions
old_friends = {
    friends[i]:ages[i]
    for i in range(len(friends))
    if ages[i] > 40
}
print(old_friends)

#zip'ing
old_friends_v2 = dict(zip(friends,ages))
print(old_friends_v2)

#enumeration
for counter, friend in enumerate(friends,start=1):
    print(counter)
    print(friend)

print(list(enumerate(friends)))
print(dict(enumerate(friends)))

#functions
car_data = [
    {"Company": "Toyota", "Model": "Camry", "Mileage": 30, "FuelConsumed": 10},
    {"Company": "Honda", "Model": "Civic", "Mileage": 25, "FuelConsumed": 12},
    {"Company": "Ford", "Model": "Escape", "Mileage": 28, "FuelConsumed": 11},
    {"Company": "Chevrolet", "Model": "Malibu", "Mileage": 26, "FuelConsumed": 13},
]

def calculate_mpg(car):
    mpg = car["Mileage"]/car["FuelConsumed"]
    name = f"{car['Company']}{car["Model"]}"
    print(f"{name} does {mpg} miles per galon ")

for car in car_data:
    calculate_mpg(car)

def add (x,y=3):
    total = x+y
    return total

print(add(5,6))

#lambda
divide = lambda x,y:x/y
print(divide(15,3))

#first-class functions
avg = lambda seq: sum(seq)/len(seq)
total = lambda seq:sum(seq)
top = lambda seq:max(seq)

operations = {
    "average":avg,
    "total":total,
    "top":top
}

student_data = [
    {"name": "John", "grades": (85, 90, 78)},
    {"name": "Alice", "grades": (92, 88, 95)},
    {"name": "Bob", "grades": (80, 75, 82)},
    {"name": "Eva", "grades": (95, 89, 91)},
]

for student in student_data:
    name = student["name"]
    grades = student["grades"]
    print(f"Student: {name}")
    operation = input("Enter 'average', 'total' or 'top': ")
    operation_function = operations[operation]
    print(operation_function(grades))
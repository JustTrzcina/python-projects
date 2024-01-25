class Location:
    def __init__(self,new_name:str,new_temp:list):
    #properties
        self.name = new_name 
        self.temperatures = new_temp
    #methods
    def avg_temp(self):
        return sum(self.temperatures)/len(self.temperatures)

first_location = Location("Warsaw",[4,5,6,4])
second_location = Location("Gdansk",[-1,2,3,0])

print(first_location.avg_temp())

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self,i):
        return self.cars[i]
    
    def __repr__(self):
        return f'<Garage {self.cars}>'
    
    def __str__(self):
        return f'Garage with {len(self)} cars'
    
ford = Garage()
ford.cars.append('Raptor')
ford.cars.append('Mondeo')
print(len(ford))
print(ford[0])
for car in ford:
    print(car)
print(ford)

class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)
    
class WorkingStudent(Student):
    def __init__(self, name,school,salary):
        super().__init__(name,school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary*40

john = WorkingStudent('John','PBS',27.70)
print(john.weekly_salary)

steve = Student('Steve','UW')
steve.marks.append(73)
steve.marks.append(87)
print(steve.average())

class FixedFloat:
    def __init__(self,amount):
        self.amount = amount

    def __repr__(self):
        return f'FixedFloat {self.amount:.2f}'
    
    @classmethod
    def from_sum (cls,value1,value2):
        return cls(value1+value2)
    
    
number = FixedFloat(17.3422)
new_number = FixedFloat.from_sum(34.345,23.231)
print(number)
print(new_number)

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol='EUR'
    def __repr__(self):
        return f'{self.symbol} {self.amount:.2f}'
money = Euro.from_sum(78.33,-32.12)
print(money)
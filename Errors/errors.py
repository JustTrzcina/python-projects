class MyError(TypeError):
    """
    Exception when a certain error code happens
    """
    def __init__(self,message,code) -> None:
        super().__init__(f'Error code {code}: {message}')
        self.message=message
err = MyError("Bruh",404)

class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def __repr__(self) -> str:
        return f'Car {self.make} {self.model}'


class Garage:
    def __init__(self):
        self.cars=[]
    def __len__(self):
        return len(self.cars)
    def add_car(self,car):
        if not isinstance(car,Car):
            raise TypeError(f'Tried to add {car.__class__.__name__} instead of "Car" object ')
        self.cars.append(car)

car = Car('Tesla',"Model S")
garage = Garage()
garage.add_car(car)

try:
    garage.add_car("tesla")
except TypeError:
    print('That was not a Car object')
finally:
    print("Finished")


class User:
    def __init__(self,name,engagement) -> None:
        self.name=name
        self.engagement=engagement
        self.score=0
    def __repr__(self) -> str:
        return f'User {self.name}'


def email_engaged_user(user):
    try:
        user.score = perform_calculation(user.engagement)
    except ValueError:
        print('Incorrect values provided to our calculation function.')
    else:
        if user.score>500:
            send_engagement_notification(user)


def get_user_score(user):
    try:
        perform_calculation(user.engagement)
    except KeyError:
        print('Incorrect values provided to our calculation function.')
        raise

def perform_calculation(metrics):
    return metrics['clicks']*5+metrics['hits']*2

def send_engagement_notification(user):
    print(f'Notification sent to {user}')

new_user = User("John",{'clicks':61,'hits':100})
email_engaged_user(new_user)


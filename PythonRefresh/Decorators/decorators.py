import functools

user= {'username':"Drew44",'access_level':'admin'}

def access_control(access_level):
    def user_has_permission(func):
        @functools.wraps(func)
        def secure_func(*args,**kwargs):
            if user.get('access_level') == access_level:
                return func(*args,**kwargs)
        return secure_func
    return user_has_permission
        
@access_control('admin')
def my_func(panel):
    return f'Password for {panel} panel = qwerty'

def another_func():
    pass

print(my_func('movies'))
print(my_func.__name__)
print(another_func())
print(another_func.__name__)




def add_all(*args):
    return sum(args)

print(add_all(6,3,3,2))

def pretty_print(**kwargs):
    for k,v in kwargs.items():
        print(f'{k} -- {v}')

pretty_print(**{"username":"andrew", "access_level":"guest"})


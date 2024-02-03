import functools

user= {'username':"Drew44",'access_level':'admin'}

def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(panel):
        if user.get('access_level') == 'admin':
            return func(panel)
    return secure_func
        
@user_has_permission
def my_func(panel):
    return f'Password for {panel} panel = qwerty'


print(my_func('movies'))
print(my_func.__name__)

my_func = user_has_permission(my_func)

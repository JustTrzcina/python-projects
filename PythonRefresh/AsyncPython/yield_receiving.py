from collections import deque
from types import coroutine

# def greet():
#     friend = yield
#     print(f'Hello, {friend}')

# g= greet()
# g.send(None) ##Priming the generator -> rund up to yield
# g.send('Steve')

friends = deque(('John','Tony','Katie','Steve','Annie'))

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print('starting...')
    await g
    print('ending...')

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')

greeting = input('Enter greeting: ')
greeter.send(greeting)

from collections import deque

# def greet():
#     friend = yield
#     print(f'Hello, {friend}')

# g= greet()
# g.send(None) ##Priming the generator -> rund up to yield
# g.send('Steve')

friends = deque(('John','Tony','Katie','Steve','Annie'))

#Corutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


# def greet(g):
#     yield from g

def greet(g):
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Multitasking')
greeter.send('How are you ')
from collections import deque

friends = deque(('John','Tony','Katie','Steve','Annie'))

def get_friend():
    yield from friends

def greet(g):
    while True:
        try:
            friend= next(g)
            yield f'Hello {friend}'
        except StopIteration:
            pass

friends_generator = get_friend()
g = greet(friends_generator)
print(next(g))
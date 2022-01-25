from collections import deque

# def greet():
#     friend = yield
#     print(f'Hello, {friend}')
#
#
# g = greet()
# g.send(None)  # <- called priming the generator
# g.send('Adam')

# ================================================
# another example:

friends = deque(('Ralph', 'Jose', 'Charlie', 'Annu', 'Supandi'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Random sentence...')
greeter.send('Hello')




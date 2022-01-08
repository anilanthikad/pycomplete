# # friend = 'saba'
# username = input('Enter you name: ')

# if username == friend:
#     print('Hello, friend!')
# else:
#     print('You are not a friend')


# print('Hello friend!') if username == friend else print('You are not a friend')
# ^ Sourcery way... Muahahaha

# =============

friends = ['rob', 'gary', 'bary']
family = ['meo', 'deo']

username = input('Enter your name: ')

if username in friends:
    print('Hello friend')
elif username in family:
    print('Hello family')
else:
    print('I don\'t know you')



# age = input('Enter you age: ')
#
# if age.isnumeric():  # isnumeric is what I forget =/
#     months = int(age) * 12
#     print(f'You have lived for {months} months.')
# else:
#     print('Please type a whole number!')

# ======================================================
#  Prime numbers:

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f'{n} equals {x} * {n//x}')
            break
    else:
        print(f'{n} is a prime number.')

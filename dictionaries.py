
# Dictionaries

# friends_ages = {
#     'Ralf': 24,
#     'Adam': 40,
#     'Sizu': 23
# }
# print(friends_ages['Sizu'])
# friends_ages['Bob'] = 56
# print(friends_ages)
# friends_ages['Bob'] = 55
# print(friends_ages)

# ------------------------

# friends = (
#     {'name': 'Boda', 'age': 45},
#     {'name': 'Soda', 'age': 5},
#     {'name': 'Beeda', 'age': 46}
# )
#
# print(friends[1]['age'])
# print(friends[2]['name'])
#
# friends_ages = [
#     ('Ralf', 24),
#     ('Adam', 40),
#     ('Sizu', 23)
# ]
# new_friends = dict(friends_ages)
# print(new_friends)

# ---------------------------------------
# To iterate over dictionaries

friend_age = {
    'Ralph': 25,
    'Anne': 37,
    'Charlie': 24,
    'Bobby': 56
}

for name in friend_age:  # reflects only the keys not the values.
    print(name)

for age in friend_age.values():  # for getting the values.
    print(age)

for key, value in friend_age.items():  # for key:value pair.
    print(f'Name is {key} and age is {value}')
    print(key, value)



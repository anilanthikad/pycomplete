# age = input('Enter you age: ')
#
# if age.isnumeric():  # isnumeric is what I forget =/
#     months = int(age) * 12
#     print(f'You have lived for {months} months.')
# else:
#     print('Please type a whole number!')

# ======================================================


# ======================================================
# Sets = no order, no duplicates.

# art_friends = {'Ralf', 'Gorgi', 'Jen'}
# science_friends = {'Mike', 'Dan', 'Jen'}

# art_friends.add('Jon')
# print(art_friends)

# ----------------------------
# Use case:
#
# art_but_not_science = art_friends.difference(science_friends)
# print(art_but_not_science)
# not_in_both = art_friends.symmetric_difference(science_friends)
# print(not_in_both)
# in_both = art_friends.intersection(science_friends)
# print(in_both)
# all_friends = art_friends.union(science_friends)
# print(all_friends)

# ====================================
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


# List comprehensions
# ===================

# numbers = [0, 1, 2, 3, 4]
# double_numbers = []

# for number in numbers:
#     double_numbers.append(numbers * 2)
#
# print(double_numbers)

# double_numbers = [number * 2 for number in range(5)]
# print(double_numbers)

# --------------------------------------------------

# friends_ages = [22, 33, 45, 35, 37, 42]
# age_string = [f'My friend is {age} years old.' for age in friends_ages]
# print(age_string)

# --------------------------------------------------

# names = ['Ralph', 'Bobby', 'Jon']
# lower = [name.lower() for name in names]
# print(lower)

# --------------------------------------------------

# friend = input('Enter you friend name: ')
# friends = ['Ralph', 'Bobby', 'Jon', 'Charlie', 'Anne']
#
# friends_lower = [name.lower() for name in friends]
#
# if friend.lower() in friends_lower:
#     print(f'{friend.title()} is one of your friends.')

# ==================================================

# List Conditional comprehensions
# ===========================

# ages = [22, 35, 56, 78, 31]
# odds = [age for age in ages if age % 2 == 1]
#
# print(odds)

# --------------------------------------------------

# friends = ['Ralph', 'Bobby', 'Jon', 'Charlie', 'Anne']
# guests = ['jose', 'mathai', 'Ralph', 'Charlie', 'Jen']
#
# friends_lower = set([f.lower() for f in friends])
# # guests_lower = set([g.lower() for g in guests])  # not needed for the comprehension method

# print(friends_lower.intersection(guests_lower))  # Cant get titlecase in this method.

# so...
# present_friends = [
#     name.title()
#     for name in guests
#     if name.lower() in friends_lower
# ]
# print(present_friends)

# ==================================================
# ==================================================

# Set and Dictionary comprehensions
# ==================================

# friends = ['Ralph', 'Bobby', 'Jon', 'Charlie', 'Anne']
# guests = ['jose', 'mathai', 'Ralph', 'Charlie', 'Jen']

# friends_lower = {f.lower() for f in friends}
# guests_lower = {g.lower() for g in guests}
#
# present_friends = {name.title()
#                    for name in friends_lower.intersection(guests_lower)}
#
# print(present_friends)

# --------------------------------------------------

friends = ['Ralph', 'Bobby', 'Jon', 'Charlie', 'Anne']
time_since_seen = [3, 7, 8, 9, 12]

long_timers = {
    friends[i]: time_since_seen[i]  # we get a dictionary
    for i in range(len(friends))
    if time_since_seen[i] > 5  # to check friends seen less than 5 years
}
print(long_timers)


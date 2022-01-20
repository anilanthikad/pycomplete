# Mutable are data which can change
# Immutable are data which cant be changed.

friends_last_seen = {
    'Ralph': 12,
    'Ann': 45,
    'Suppa': 15
}

print(id(friends_last_seen))

friends_last_seen['Ralph'] = 0

print(id(friends_last_seen))

"""
The function which use the same memory id after a change in data is = mutable

These are the immutable types

-> integers -> all functions return new int objects.
-> floats
-> tuples
-> strings
"""


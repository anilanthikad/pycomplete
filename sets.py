# Sets = no order, no duplicates.

art_friends = {'Ralf', 'Gorgi', 'Jen'}
science_friends = {'Mike', 'Dan', 'Jen'}

# art_friends.add('Jon')
# print(art_friends)

# ----------------------------
# Use case:

art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)
in_both = art_friends.intersection(science_friends)
print(in_both)
all_friends = art_friends.union(science_friends)
print(all_friends)

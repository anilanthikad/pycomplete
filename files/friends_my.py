# Ask user for a list of three friends
# For each friend, we'll tell the user whether they are in nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

# hint: readlines()

# ===============================
# My attempt
# ===============================
nearby_friends = []

user_friend1 = input('Enter first friends name: ')
user_friend2 = input('Enter second friends name: ')
user_friend3 = input('Enter third friends name: ')

nearby_friends.append(user_friend1)
nearby_friends.append(user_friend2)
nearby_friends.append(user_friend3)

# print(nearby_friends)

people_list = open('people.txt', 'r')
people_content = people_list.read()


# print(people_content)

for name in nearby_friends:
    if name in people_content:
        # add_name = []
        nrby_frnds = open('nearby_friends.txt', 'a')
        nrby_frnds.write(f'{name}\n')
        nrby_frnds.close()

        # add_name.append(name)
# people_content.close()

nearby_list = open('nearby_friends.txt', 'r')
final_list = nearby_list.read()
nearby_list.close()
people_list.close()
print(final_list)

# ==========================================================

nearby_friends = []

user_friend1 = input('Enter first friends name: ')
user_friend2 = input('Enter second friends name: ')
user_friend3 = input('Enter third friends name: ')

nearby_friends.append(user_friend1)
nearby_friends.append(user_friend2)
nearby_friends.append(user_friend3)

with open('people.txt', 'r') as people_list:
    people_content = people_list.read()


    for name in nearby_friends:
        if name in people_content:
            with open('nearby_friends.txt', 'a') as nrby_frnds:
                nrby_frnds.write(f'{name}\n')
    with open('nearby_friends.txt', 'r') as nearby_list:
        final_list = nearby_list.read()
print(final_list)



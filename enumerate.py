
top_friends = ['ralph', 'suzi', 'annie', 'james', 'mike', 'randi']

# for i in range(3):
#     print(f'My top {i+1} friend is {top_friends[i]}.')

for i, friend in enumerate(top_friends):
    print(f'My top {i+1} friend is {friend}.')

friend_g = enumerate(top_friends)
print(next(friend_g))
k, v = next(friend_g)
print(k)
print(v)

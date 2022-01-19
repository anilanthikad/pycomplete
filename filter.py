
def starts_with_r(friend):
    return friend.startswith('r')


friends = ['ralph', 'suzi', 'annie', 'james', 'mike', 'randi']

# start_with_r = filter(starts_with_r, friends)  # arg1: function that returns with
# True/False

start_with_r = filter(lambda x: x.startswith('r'), friends)  # with lambda

another_starts_with_r = (f for f in friends if f.startswith('r'))

# print(next(start_with_r))
print(list(start_with_r))



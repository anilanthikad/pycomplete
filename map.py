

friends = ['ralph', 'suzi', 'annie', 'james', 'mike', 'randi']

# start_with_r = filter(starts_with_r, friends)

start_with_r = filter(lambda x: x.startswith('r'), friends)

another_starts_with_r = (f for f in friends if f.startswith('r'))

friends_upper = map(lambda x: x.upper(), friends)  # use this only if your team is
# used to using map.
friends_upper = [friend.upper() for friend in friends]
friends_upper = (friend.upper() for friend in friends)  # best to use this at all times

print(next(friends_upper))

# ===========================


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


users = [
    {'username': 'ralph', 'password': '123'},
    {'username': 'dubukku', 'password': 'youknow'}
]

users = [User.from_dict(user) for user in users]
users = map(User.from_dict, users)


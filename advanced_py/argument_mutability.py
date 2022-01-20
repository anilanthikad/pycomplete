

friends_last_seen = {
    'Ralph': 12,
    'Ann': 45,
    'Suppa': 15
}


def see_friend(friends, name):
    print(id(friends))
    friends[name] = 0


see_friend(friends_last_seen, 'Ralph')

# =====================================

age = 20

def increase_age(current_age):
    current_age = current_age + 1

print(id(age))
increase_age(age)
print(id(age))

# =====================================

primes = [2, 3, 5]
print(id(primes))

primes += [7, 11]
print(id(primes))

primes = [7, 11] + [13, 15]
print(id(primes))




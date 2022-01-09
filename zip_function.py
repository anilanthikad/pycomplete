
friends = ['Ralph', 'Bobby', 'Jon', 'Charlie', 'Anne']
time_since_seen = [3, 7, 8, 9, 12]

# >>>> Zip combines 2 or more lists into one list.

long_timers_dict = dict(zip(friends, time_since_seen))
long_timers_list = list(zip([1, 2, 3, 4, 5, 6], friends, time_since_seen))

print(long_timers_dict)
print(long_timers_list)

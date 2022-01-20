"""
-> counter -> counts items in a iterable or like dictionary.
-> defaultdict ->
-> ordereddict
-> namedtuple
-> deque
"""

from collections import *
#
# device_temperature = [13.5, 14.0, 14.0, 14.5, 15.0, 16.0]
#
# temperature_counter = Counter(device_temperature)
# print(temperature_counter[14.0])

# =========================================================

# coworkers = [('ralph', 'MIT'), ('Janny', 'MIT'), ('ralph', 'Singapore'), ('unga',
#                                                                         'malgudi')]
# alma_maters = defaultdict(list)
#
# for coworker, place in coworkers:
#     alma_maters[coworker].append(place)
#
# print(alma_maters['ralph'])
# print(alma_maters['MIT'])

# --------------------------------------------

# my_company = 'Teclado'
#
# coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
# other_coworkers = [('Ralph', 'app.inc'), ('Anna', 'shitgle')]
#
# coworker_companies = defaultdict(lambda: my_company)
#
# for person, company in other_coworkers:
#     coworker_companies[person] = company
#
# print(coworker_companies[coworkers[0]])
# print(coworker_companies[other_coworkers[0][0]])

# =========================================================

# o = OrderedDict()
# o['Ralph'] = 6
# o['Jose'] = 16
# o['Jenny'] = 8
#
# print(o)
#
# o.move_to_end('Ralph')
# print(o)

# =========================================================

# account = ('checking', 1650.00)
#
# Account = namedtuple('Account', ['name', 'balance'])
#
# accountNamedTuple = Account(*account)
#
# print(accountNamedTuple._asdict()['balance'])

# =========================================================

friends = deque(('Jen', 'Li', 'Charlie', 'Rhys'))
friends.append('Jose')
friends.appendleft('Anto')
print(friends)

friends.pop()
friends.popleft()

print(friends)



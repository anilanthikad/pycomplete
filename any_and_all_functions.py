

friends = [
    {
        'name': 'Ralph',
        'location': 'Wash DC'
    },
    {
        'name': 'Supandi',
        'location': 'Ejipu'
    },
    {
        'name': 'Dubukku',
        'location': 'Ejipu'
    },
    {
        'name': 'Mike',
        'location': 'USA'
    }
]

your_location = input('Where are you right now?: ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):  # any will be True if there is at-least 1.
    print('You are not alone')

"""
These evaluate Falsy (Truthy/Falsy)

- 0, 0.0
- None
- [], (), {}
- False
"""

print(all([0, 1, 2, 3, 4, 5]))  # <- will shoe False cos '0' in it.


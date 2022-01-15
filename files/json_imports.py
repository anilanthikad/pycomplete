import json

# with open('friends_json.txt', 'r') as file:
#     file_content = json.load(file)  # reads file and turns it into a dictionary.

# print(file_content['friends'][1])

# ================================================

# cars = [
#     {'make': 'ford', 'model': 'shit'},
#     {'make': 'toyota', 'model': 'another shit'},
#     {'make': 'jeep', 'model': 'best'}
# ]
#
# with open('cars_json.txt', 'w') as file:
#     json.dump(cars, file)


# ================================================
# "loads" to change a json str to dict

my_json_string = '[{"name": "Ding Dong", "released": 1940}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])


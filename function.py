# def greet():
#     name = input('What is your name?: ')
#     print(f'Hello, {name}')
#
# greet()

# -----------------------------------------------

# Arguments and Parameters

# cars = [
#     {'make': 'Ford', 'model': 'Fiesta', 'mileage': 23000, 'fuel_consumed': 460},
#     {'make': 'Ford', 'model': 'Focus', 'mileage': 17000, 'fuel_consumed': 40},
#     {'make': 'Merc', 'model': 'Mx-Shit', 'mileage': 2300, 'fuel_consumed': 60},
#     {'make': 'Mazda', 'model': 'Super', 'mileage': 2300456, 'fuel_consumed': 40}
# ]
#
# def calculate_mpg(car_to_calc):
#     mpg = car_to_calc['mileage'] / car_to_calc['fuel_consumed']
#     name = f"{car_to_calc['make']} {car_to_calc['model']}"
#     print(f'{name} does {mpg} miles per gallon.')
#
# calculate_mpg(cars[3])  # for single car
# # or...
# for car in cars:  # for the entire dictionary
#     calculate_mpg(car)

# -----------------------------------------------
# Return values

cars = [
    {'make': 'Ford', 'model': 'Fiesta', 'mileage': 23000, 'fuel_consumed': 460},
    {'make': 'Ford', 'model': 'Focus', 'mileage': 17000, 'fuel_consumed': 40},
    {'make': 'Merc', 'model': 'Mx-Shit', 'mileage': 2300, 'fuel_consumed': 60},
    {'make': 'Mazda', 'model': 'Super', 'mileage': 2300456, 'fuel_consumed': 40}
]

def calculate_mpg(car):
    mpg = car['mileage'] / car['fuel_consumed']
    return mpg


def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)
    return f'{name} does {mpg} miles per gallon.'



calculate_mpg(cars[3])  # for single car
# or...
for car in cars:  # for the entire dictionary
    print(print_car_info(car))



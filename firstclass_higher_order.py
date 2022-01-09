# def greet():
#     print('Hey there')

# 'greet' without () is still a function but doesn't run.
# the () is what makes it run.

# hello = greet
#
# hello()  # This is a first class function

# --------------------------------------------------------

# Usecase...

# def before_and_after(func):
#     print('Before...')
#     func()
#     print('After...')
#
#
# def greeting():
#     print('Hello')
#
#
# before_and_after(greeting)

# --------------------------------------------------------
# Higher order functions...

operations = {
    'average': lambda seq: sum(seq) / len(seq),
    'total': sum,  # lambda seq: sum(seq),
    'top': max  # lambda seq: max(seq)
}

students = [
    {'name': 'Ralph', 'grade': (67, 90, 95, 100)},
    {'name': 'Suzi', 'grade': (37, 70, 9, 10)},
    {'name': 'Supandi', 'grade': (73, 79, 39, 70)},
    {'name': 'Supandi', 'grade': (79, 98, 56, 50)},
]

for student in students:
    name = student['name']
    grade = student['grade']

    print(f'Student: {name}')
    operation = input('Enter, "average", "total" or "top": ')

    result = operations[operation](grade)
    print(result)

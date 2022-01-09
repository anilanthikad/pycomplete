# def divide(x, y):
#     return x / y


# divide = lambda x, y: x / y
#
# print(divide(16, 9))

# -----------------------------------------

# def average(sequence):
#     return sum(sequence) / len(sequence)

average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {'name': 'Ralph', 'grade': (67, 90, 95, 100)},
    {'name': 'Suzi', 'grade': (37, 70, 9, 10)},
    {'name': 'Supandi', 'grade': (73, 79, 39, 70)},
    {'name': 'Supandi', 'grade': (79, 98, 56, 50)},
]

for student in students:
    print(average(student['grade']))

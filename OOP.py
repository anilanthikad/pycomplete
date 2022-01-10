my_student = {
    'name': 'Ralph Chan',
    'grades': [70, 88, 90, 99]
}


def avg_grade(student):
    return sum(my_student['grades']) / len(my_student['grades'])


class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name  # called  properties
        self.grades = new_grades  # called  properties

    def average(self):  # called  methods
        return sum(self.grades) / len(self.grades)


student_one = Student('Ralph Chan', [70, 88, 90, 99])
student_two = Student('Supandi', [90, 98, 99, 100])

# print(student_one.name)
# print(student_two.name)
print(student_two.name, student_two.average())


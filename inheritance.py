class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 37.5


ralph = WorkingStudent('Ralph', 'MIT', 15.50)
print(ralph.salary)

ralph.marks.append(57)
ralph.marks.append(99)
print(ralph.average())
print(ralph.weekly_salary())



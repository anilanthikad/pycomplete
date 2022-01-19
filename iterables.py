# REMEMBER!!!!!!
# Iterator: used to get next value.
# Iterable: used to go over all the values of the iterator (loop).


class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):  # next(my_object)
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self


# class FirstHundredIterable:
#     def __iter__(self):
#         return FirstHundredGenerator()


# print(sum(FirstHundredGenerator()))
#
# for i in FirstHundredGenerator():
#     print(i)


class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Foarar']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


for car in AnotherIterable():
    print(car)


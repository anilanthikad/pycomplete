class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):  # next(my_object)
        if self.number >= 100:
            raise StopIteration()
        current = self.number
        self.number += 1
        return current

        # if self.number < 100:  # same as above block
        #     current = self.number
        #     self.number += 1
        #     return current
        # else:
        #     raise StopIteration()


my_gen = FirstHundredGenerator()
print(my_gen.number)
next(my_gen)
print(my_gen.number)
print(next(my_gen))
print(next(my_gen))



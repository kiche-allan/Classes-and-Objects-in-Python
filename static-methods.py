class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print("Bark")

#class variables
#when accessing them one doesnt need to have an instance of an object

# tim = Dog("Tim")
# jim = Dog('Jim')
# print(Dog.dogs)
#static methods do not need the class to be called
# tim = Dog('tim')
# print(Dog.num_dogs())


class Math:
    @staticmethod
    def add(x, x2):
        return x + x2
Dog.bark(5)
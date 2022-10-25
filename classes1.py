#creating own objects and classes
class Dog(object):
    def __init__(self, name, age):
        #the self in here is called the attribute
        #attributes are kind of like variables that belong to an object
        #create it with a self attribute using an instance of a class

        self.name = name
        self.age = age
        self.li = [1, 3, 5, 7]

    def speak(self):
        print("Hi I am ", self.name, 'and I am', self.age, 'years old')

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight

tim = Dog('Tim', 23)
fred = Dog('Fred', 21)
tim.change_age(5)
tim.add_weight(90)
print(tim.age)
#by simply calling the atrribute of the name, we can access it
tim.speak()
fred.speak()

print(tim.li)
#the benefits of classes is that u can store multiple instances of objects
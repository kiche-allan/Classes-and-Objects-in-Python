#creating own objects and classes
class Dog(object):
    def __init__(self, name, age):
        #the self in here is called the attribute
        #attributes are kind of like variables that belong to an object
        #create it with a self attribute using an instance of a class

        self.name = name
        self.age = age


    def speak(self):
        print("Hi I am ", self.name, 'and I am', self.age, 'years old')

    def talk(self):
        print('Bark!')
    #when talking about inheritance, there is a super class and then the child class

class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    # def speak(self):
                                                                                                                                                                                                                                                                                                                                                                `
    def talk(self):
        print('meow!')



jim = Dog('jim', 70)
jim.talk()

tim = Cat('tim', 6, 'red')
tim.talk()
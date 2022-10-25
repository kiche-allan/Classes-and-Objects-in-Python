#creating own objects and classes
class Dog(object):
    def __init__(self):
        #the self in here is called the attribute
        #attributes are kind of like variables that belong to an object
        #create it with a self attribute using an instance of a class

        pass

    def speak(self):
        print("Hi I am ", self.name)

tim = Dog('Tim')
fred = Dog('Fred')
tim.speak()
fred.speak()

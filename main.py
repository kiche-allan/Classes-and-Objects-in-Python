x = 5
y = 'hello classes'
import turtle


tim = turtle.Turtle()
# print(type(x))
# print(type(y))


# difference between functions and methods
# function is created with a def keyword
# a method is what we call with a dot operator
print(y.upper())

print(y.replace('c', 'err'))
def func(x):
    return x + 1

print(func(5))
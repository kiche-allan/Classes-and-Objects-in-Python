class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x +=x
        self.y +=y

    def __add__(self, p):
        return Point(self.x + p.x, self.y +p.y)
    def __sub__(self, p):
        return Point(self.x -p.x, self.y - p.y)
    def __mul__(self, p):
        return self.x * p.x + self.y * p.y
    #comparing points

    #defining the lengths
    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
    #greater than
    def __gt__(self, p):
        return self.length() > p.length()

    #greater or equal to
    def __ge__(self, p):
        return self.length() >= p.length()
    ##lesser than
    def __lt__(self, p):
        return self.length() < p.length()
    #less or equal to
    def __len__(self, p):
        return self.length() <= p.length()
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) + ')'

p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 4)
p4 = Point(0, 1)
p5 = p1 + p2
p6 = p4 - p1
p7 = p2 * p3

print(p1 ==p2)
print(p1 > p2)
print(p4 <= p3)
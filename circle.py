class Circle:
    radius = 0

    def __init__(self, r):
        self.radius = r

    def circumfrence(self):
        return 3.141 * 2 * self.radius

circleA = Circle(15)
circleB = Circle(19.5)

print("Circle A cicumfrence: " + str(circleA.circumfrence()))
print("Circle B cicumfrence: " + str(circleB.circumfrence()))

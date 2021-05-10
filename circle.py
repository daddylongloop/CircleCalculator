import math

while True:
    radius = float(input('Enter the radius of a circle: '))
    def Circumference(radius):
        return 2 * math.pi * radius

    def Area(radius):
        return math.pi * radius * radius

    circumference = Circumference(radius)
    area = Area(radius)

    print(" Circumference Of a Circle = %.2f" % circumference)
    print(" Area Of a Circle = %.2f\n" % area)


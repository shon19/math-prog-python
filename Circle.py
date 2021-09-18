import math


class Circle():

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def get_diameter(self):
        return 2 * self.radius


def main():
    circ = Circle(radius=7)
    print("Area of the circle: ", circ.area())
    print("Circumference of the circle is: ", circ.circumference())
    print("Diameter of the circle is: ", circ.get_diameter())


if __name__ == "__main__":
    main()
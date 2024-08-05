# TODO: Add code here
# IMPORTS
import math
import matplotlib as plt


class Point:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = x
#Una clase Circle con los atributos center de tipo Point y
# radius de tipo float. Ambos atributos deben ser inicializados con parámetros en el constructor.
class Circle:
    def __init__(self, center:Point, radius:float):
        self.center = center
        self.radius = radius

#Method circle area
    def area(self) -> float:
        area_circle = math.pi * self.radius**2
        return area_circle

#Method to draw a circle
    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

#Dunder method to representate the circle in format chain
    def  __str__(self) -> str:
        x, y = self.center
        return f"Circle with center at ({x}, {y}) and radius {self.radius}"

class Triangle:
    def __init__(self, point_1: tuple, point_2: tuple,  point_3: tuple):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def area(self) -> float:
        x1, y1 = self.point_1
        x2, y2 = self.point_2
        x3, y3 = self.point_3
        area_triangle = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        return area_triangle


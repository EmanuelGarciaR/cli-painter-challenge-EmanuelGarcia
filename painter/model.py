# TODO: Add code here
# IMPORTS
import math


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
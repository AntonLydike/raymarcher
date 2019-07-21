from vectormath import Vector3
import numpy as np

class Shape:
    def __init__(self, color: list):
        self.color = color;

    def distance(self, point: Vector3) -> float:
        return 10.0

    def getColor(self, point: Vector3, direction: Vector3) -> list:
        return self.color

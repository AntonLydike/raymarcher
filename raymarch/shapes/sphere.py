from vectormath import Vector3
import numpy as np

from .shape import Shape

class Sphere(Shape):
    """Create a new sphere with a radius, center and a color (defaults to white)"""
    def __init__(self, center: Vector3, radius: float, color = [255,255,255]):
        Shape.__init__(self, color)
        self.center = center;
        self.radius = radius

    """get the distance from a point in space to the surface of the sphere"""
    def distance(self, point: Vector3, dist) -> float:
        return dist(self.center, point) - self.radius

    """get the color of the sphere at a point and with a direction"""
    def getColor(self, point: Vector3, direction: Vector3) -> list:
        # effect strength (between 0 and 1)
        strength = .7

        angle = direction.angle(point - self.center, unit='deg') % 180 - 90;

        if (angle < 0.1):
            return self.color

        # calculate brightness based on the angle and the effect strength
        brightness = 1 - ((1 - abs(angle / 90)) * strength)

        # apply some darkening depending on the angle of the ray
        return np.array(self.color) * brightness

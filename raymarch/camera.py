from vectormath import Vector3
from math import cos, sin
import numpy

from .ray import Ray

"""convert degrees to radians"""
def deg_to_rad(deg: int) -> float:
    return deg * numpy.pi / 180

"""convert radians to degrees"""
def rad_to_deg(rad: float) -> int:
    return rad * 180 / numpy.pi

"""rotate around the z axis"""
def rotate_z(pt: Vector3, rad: float) -> Vector3:
    x_ = pt.x * cos(rad) - pt.y * sin(rad)
    y_ = pt.x * sin(rad) + pt.y * cos(rad)

    pt.x = x_
    pt.y = y_

    return pt;

"""rotate around the x axis"""
def rotate_x(pt: Vector3, rad: float) -> Vector3:
    y_ = pt.y * cos(rad) - pt.z * sin(rad)
    z_ = pt.y * sin(rad) + pt.z * cos(rad)

    pt.y = y_
    pt.z = z_

    return pt;

"""A Camera has a resolution, a field of view, an origin and a direction"""
class Camera:
    """Create new camera"""
    def __init__(self, width: int, height: int, fov: int, origin: Vector3, direction: Vector3):
        self.width = width
        self.height = height
        self.fov = fov
        self.origin = origin

        direction.normalize()
        self.direction = direction

    """This is an iterator over all rays being cast for an image"""
    def rays(self, scene):
        longestEdge = max(self.width, self.height)
        fov_hor = self.fov * self.width / longestEdge
        fov_vert = self.fov * self.height / longestEdge

        for x in range(0, self.width):
            for y in range(0, self.height):
                direction = Vector3(self.direction)
                rotate_z(direction, deg_to_rad(fov_hor  * ((x / self.width ) - 0.5)))
                rotate_x(direction, deg_to_rad(fov_vert * ((y / self.height) - 0.5)))
                yield (x, y, Ray(Vector3(self.origin), Vector3(direction), scene))

from vectormath import Vector3
from scipy.misc import toimage
from multiprocessing import Pool as ThreadPool
import numpy as np

from .camera import Camera

def march_task(task):
    return (task[0], task[1], task[2].march())


def p_dist(p):
    # check for infinity norm
    if p == 1e368:
        return lambda a, b: max(np.abs(a - b))
    # check for euclidian norm
    if p == 2:
        return lambda a, b: (a-b).length

    return lambda a, b : sum(np.abs(a - b) ** p) ** (1/p)


class Scene:
    poolsize = 8

    def __init__(self, camera: Camera, shapes: list, background: list, p_norm = 2):
        self.shapes = shapes
        self.camera = camera
        self.background = background
        self.p_norm = p_norm

    def draw(self):
        data = np.zeros((self.camera.height, self.camera.width, 3), dtype=np.uint8)

        pool = ThreadPool(self.poolsize)

        print("Strarting pool")

        for result in pool.imap_unordered(march_task, self.camera.rays(self), 64):
            (x, y, color) = result
            data[y,x] = color
            # print(color)

        print("pool finished")

        img = toimage(data)
        img.save('out.png')

    def nearest(self, pt: Vector3) -> tuple:
        # get the distance function
        dist_f = p_dist(self.p_norm)


        # initial shape
        find = (None, 1e309)

        for shape in self.shapes:
            dist = shape.distance(pt, dist_f)
            if dist < find[1]:
                find = (shape, dist)

        return find

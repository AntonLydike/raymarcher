from raymarch import *
from raymarch.shapes import Sphere
from vectormath import Vector3

# create some spheres
shapes = [Sphere(Vector3(0,0,0), 1), Sphere(Vector3(1,0,0), 0.5, [255, 100, 100]), Sphere(Vector3(-1,0,0), 0.5, [100,100,255])]

# create the camera
camera = Camera(1080, 720, 90, Vector3(0, 3, 0), Vector3(0, -1, 0))

# create the scene with a black background
# if you want, you can specify a special norm by specifing p_norm=1 (or any other value > 0)
scene = Scene(camera, shapes, [0,0,0])

# set the number of threads you want to spawn
#scene.poolsize = 4

# draw the scene
scene.draw()

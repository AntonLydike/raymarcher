from vectormath import Vector3

"""This class handles the rays being cast"""
class Ray:
    """The threshold when the ray decides it "hit" something"""
    threshold = 0.02
    """The maximum nuumber of steps we take"""
    limit = 32

    """Create a new Ray which originates at origin and looks in a direction. This ray is specific to a scene"""
    def __init__(self, origin: Vector3, direction: Vector3, scene):
        self.origin = origin
        self.direction = direction
        self.scene = scene

    """march over the scene"""
    def march(self):
        pos = self.origin
        dir = self.direction

        # closest encounter of the ray
        closest = 1e386;

        for step in range(0, self.limit):
            (shape, dist) = self.scene.nearest(pos)
            if (dist < self.threshold):
                if step > 20:
                    print(str(step) + ':', end='', flush=True)
                return shape.getColor(pos, dir)
            if dist < closest:
                closest = dist;
                # print("getting closer: " + str(dist));

            pos = (pos + dir.as_length(dist))

        # print("missed by " + str(closest))
        # print(',', end='', flush=True)
        return self.scene.background

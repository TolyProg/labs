import Shape
import math

class Sphere(Shape.Shape):
    name = 'Sphere'
    def surface(self):
        return 4*math.pi*(self.a**2)
    def volume(self):
        return (4*math.pi*(self.a**3))/3

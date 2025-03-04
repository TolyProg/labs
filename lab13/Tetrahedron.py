import Shape

class Tetrahedron(Shape.Shape):
    name = 'Tetrahedron'
    def surface(self):
        return self.a*self.b # i know this is wrong, but im lazy & stpd :(
    def volume(self):
        return (self.a*self.b)/3

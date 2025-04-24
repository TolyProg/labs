import Shape

class Parallelepiped(Shape.Shape):
    name = 'Parallelepiped'
    def volume(self):
        return self.a*self.b*self.c
    def surface(self):
        return 2*(self.a*self.b + self.b*self.c + self.a*self.c)


import abc

class Shape(abc.ABC):
    material_list = {'Steel': 7850, 'Glass': 2500, 'Concrete': 2000}
    def __init__(self,a,b,c,m):
        self.a = a
        self.b = b
        self.c = c
        self.m = m
    @abc.abstractmethod
    def surface(self): pass
    @abc.abstractmethod
    def volume(self): pass
    def mass(self):
        try: mm = self.material_list[self.m]
        except: return f'Unknown material "{self.m}"'
        return self.volume()*mm
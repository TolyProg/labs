def dec(x):
    x.__call__ = x.do
    return x

@dec
class Line:
    def __init__(self, namepath):
        self.f = open(namepath, 'r')
    def do(self):
        return self.f.readline()

f = Line('max1.py')
print(f())
print(f())
print(f())
print(f())

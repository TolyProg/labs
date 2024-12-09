def dec(x):
    x.__call__ = x.do
    return x

@dec
class Log:
    def __init__(self, f):
        self.f = f
    def do(self, *args, **kwargs):
        r = self.f(*args, **kwargs)
        print('LOG:', self.f.__name__ + \
            '(' + str(args)[1:-1] + ') =', r)
        return r

def add(x, y): return x + y

f = Log(add)
print(f(1, 2))
print(f(3, 4))
print(f(128, 256))

def log(f):
    def d(*args, **kwargs):
        r = f(*args, **kwargs)
        print('LOG:', f.__name__ + \
            '(' + str(args)[1:-1] + ') =', r)
        return r
    return d

def add(x, y): return x + y

f = log(add)
print(f(1, 2))
print(f(3, 4))
print(f(128, 256))

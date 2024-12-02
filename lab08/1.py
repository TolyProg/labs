def line(fname):
    f = open(fname, 'r')
    return lambda: f.readline()

f = line('1.py')
print(f())
print(f())
print(f())

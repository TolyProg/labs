def line(fname):
    f = open(fname, 'r')
    return lambda: f.readline()

if __name__ == '__main__':
	f = line('lab8.py')
	print(f())
	print(f())
	print(f())

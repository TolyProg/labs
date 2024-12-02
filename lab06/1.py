from itertools import *

l = ['А', 'Н', 'Д', 'Р', 'Е', 'Й']
def p(x):
    if x[0] == 'Й': return False
    if x[-1] == 'Й': return False
    if x.count('Й') > 1: return False
    s = ''.join(x)
    return s.count('ЕЙ') + s.count('ЙЕ') == 0

print(len(list(filter(p, product(l, repeat=6)))))

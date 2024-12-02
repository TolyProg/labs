def w(i):
    if i == 1: return 0.3
    if i == 2: return -1.5
    p = -1.5
    pp = 0.3
    for i in range(3, i+1):
        t = p*pp*(i-2)**2/(i+1)**3
        pp = p
        p = t
    return p

for i in range(1, 10):
    print(w(i))


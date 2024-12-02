def w(i):
    if i == 1: return 0.3
    if i == 2: return -1.5
    return w(i-1)*w(i-2)*(i-2)**2/(i+1)**3

for i in range(1, 10):
    print(w(i))

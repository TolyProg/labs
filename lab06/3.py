def isPrime(x):
    if x == 1: return False
    for i in range(2,x//2+1):
        if x % i == 0: return False
    return True

# для проверки
#for i in range(1,100):
#    if(isPrime(i)): print(i)
#f = 5
#t = 9

f = 245_690
t = 245_756
for i in filter(isPrime, range(f, t)):
    print(i-f+1, i)

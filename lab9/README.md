# Лабораторная работа №9
## Вариант 3
Задача: написать генератор простых чисел

## Решение
```python
# генерирует простые числа от 2 до n (включительно)
def f(n):
    def isPrime(x):
        for i in range(2, x//2+1):
            if x % i == 0: return False
        return True
    for i in range(2, n+1):
        if isPrime(i):
            yield i

for i in f(20):
    print(i)
```

![](screen.png)

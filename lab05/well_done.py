import matplotlib.pyplot as plt
import numpy as np
from math import *

# задал верхнюю часть функции из варианта 3
def f(x):
    return cos(x)*exp(-x**2)

# создал список точек от -3 до 3 (1000 точек)
x = np.linspace(-3, 3, 1000)

# вывод в формате CSV
print('x, f(x)')
for i in x: 
    print(i, ',', f(i))

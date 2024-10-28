import matplotlib.pyplot as plt
import numpy as np
from math import *

# задал функцию из варианта 3
def f(x):
    if x > 0 and x <= 1.1:
        return cos(x)*exp(sqrt((-x)**2))
    elif x >= 1 and x <= 2:
        return log(x+1)-sqrt(4-(x**2))
    return 0

# создал список точек от -3 до 3 (1000 точек)
x = np.linspace(-3, 3, 1000)
# список точек функции из варианта
y1 = [f(i) for i in x]
# касательная по высшей точке функции из варианта
y2 = [max(y1) for i in x]

# заголовок
plt.title('Лабораторная работа 4, вариант 3')
# название осей
plt.xlabel('x')
plt.ylabel('y')
# включение сетки
plt.grid()
# построение этих функций
plt.plot(x, y1, label='Функция из варианта')
plt.plot(x, y2, 'r', label='Касательная к ней')
# аннотация
plt.text(0.785, max(y1)+0.01, 'точка касания')
# легенда
plt.legend()
# вывести график
plt.show()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['papa', 'mama', 'ya']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['papa', 180],
    ['mama', 170],
    ['ya', 185]
]

def f():
    # Выведите на консоль рост отца в формате
    #   Рост отца - ХХ см
    print('Рост отца -', my_family_height[0][1], 'см')
    # Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
    #   Общий рост моей семьи - ХХ см
    r = 0
    for i in my_family_height:
        r += i[1]
    print('Общий рост моей семьи -', r, 'см')

f()

def test(capfd):
    f()
    out, err = capfd.readouterr()
    assert out == 'Рост отца - 180 см\n\
Общий рост моей семьи - 535 см\n'
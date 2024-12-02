#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f():
    # есть список животных в зоопарке
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

    # посадите медведя (bear) между львом и кенгуру
    #  и выведите список на консоль
    zoo.insert(1, "bear")
    print(zoo)

    # добавьте птиц из списка birds в последние клетки зоопарка
    birds = ['rooster', 'ostrich', 'lark', ]
    #  и выведите список на консоль
    for i in birds:
        zoo.append(i)
    print(zoo)

    # уберите слона
    #  и выведите список на консоль
    zoo.pop(zoo.index("elephant"))
    print(zoo)

    # выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
    # Номера при выводе должны быть понятны простому человеку, не программисту.
    for i in ["lion", "lark"]:
        print(zoo.index(i))

f()

def test(capfd):
    f()
    out, err = capfd.readouterr()
    assert out == "['lion', 'bear', 'kangaroo', 'elephant', 'monkey']\n\
['lion', 'bear', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark']\n\
['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']\n\
0\n\
6\n"

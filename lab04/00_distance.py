#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

def dist(i, j):
    x1, y1 = sites[i]
    x2, y2 = sites[j]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

names = sites.keys()
for i in names:
    distances[i] = dict((j, dist(i, j)) for j in names)

print(distances)

def test():
    assert distances == {'Moscow': {'Moscow': 0.0, 'London': 145.60219778561037, 'Paris': 130.38404810405297}, 'London': {'Moscow': 145.60219778561037, 'London': 0.0, 'Paris': 42.42640687119285}, 'Paris': {'Moscow': 130.38404810405297, 'London': 42.42640687119285, 'Paris': 0.0}}

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
#garden_set = dict()
#for i in garden:
#    garden_set.setdefault(i, 0)
#    garden_set[i] += 1
#meadow_set = dict()
#for i in meadow:
#    meadow_set.setdefault(i, 0)
#    meadow_set[i] += 1
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
print(garden_set.union(meadow_set))

# выведите на консоль те, которые растут и там и там
print(garden_set.intersection(meadow_set))

# выведите на консоль те, которые растут в саду, но не растут на лугу
print(garden_set.difference(meadow_set))

# выведите на консоль те, которые растут на лугу, но не растут в саду
print(meadow_set.difference(garden_set))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Садовые цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
# Луговые цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
# Множество цветов
garden_set = set(garden)
meadow_set = set(meadow)

# Все виды цветов
print(garden_set.union(meadow_set))

# Растут и там, и там
print(garden_set & meadow_set)

# Растут в саду, но не растут на лугу
print(garden_set - meadow_set)

# Растут на лугу, но не растут в саду
print(meadow_set - garden_set)
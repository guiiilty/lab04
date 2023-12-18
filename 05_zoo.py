#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Cписок животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Посадим медведя между львом и кенгуру
zoo.insert(1, 'bear')
print(zoo)

# Добавим птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
zoo.extend(birds)
print(zoo)

# Уберём слона
zoo.remove('elephant')
print(zoo)

# Выведем на консоль в какой клетке сидит лев и жаворонок
print("Лев сидит в клетке №" + str(zoo.index('lion')+1))
print("Жаворонок сидит в клетке №" + str(zoo.index('lark')+1))
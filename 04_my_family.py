#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# моя семья (можно я не буду 9 человек расписывать)
my_family = ['Папа', 'Мама', 'Я']
my_family_height = [['Папа', 172], ['Мама', 169], ['Я', 179]]

print('Рост отца -', my_family_height[0][1], 'см')

family_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]
print('Общий рост моей семьи -', family_height, 'см')
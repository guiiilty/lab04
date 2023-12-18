#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Cписок песен группы Depeche Mode со временем звучания с точностью до долей минут
vsl = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
time_vsl = vsl[3][1] + vsl[5][1] + vsl[8][1]
print('Три песни звучат ' + str(round(time_vsl, 2)) + ' минут')

# Cловарь песен группы Depeche Mode
vsd = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
time_vsd = vsd['Sweetest Perfection'] + vsd['Policy of Truth'] + vsd['Blue Dress']
print('А другие три песни звучат ' + str(round(time_vsd, 2)) + ' минут')
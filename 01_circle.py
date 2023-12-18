#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r = 42
pi = 3.1415926
s = pi * r**2
print(round(s, 4))

point_1 = (23, 34)
dist_1 = ((point_1[0] ** 2 + point_1[1] ** 2) ** 0.5)
if dist_1 < r:
    print(True)
else:
    print(False)

point_2 = (30, 30)
dist_2 = ((point_2[0] ** 2 + point_2[1] ** 2) ** 0.5)
if dist_2 < r:
    print(True)
else:
    print(False)



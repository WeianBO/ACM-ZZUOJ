#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'
from math import sqrt

a = input().split()
x1 = int(a[0])
x2 = int(a[1])
y1 = int(a[2])
y2 = int(a[3])

def compare(m):
    if int(m) >= 0 and int(m) <= 100:
        return 1
    else:
        return 0


if 0 not in list(map(compare, a)):
    d = (y1 - x1) ** 2 + (y2 - x2) ** 2
    print("%0.2f" % sqrt(d))
else:
    pass


# for m in list(map(compare, a)):
#     print(type(m))
#     输出 int


# or pow(m,1/2)
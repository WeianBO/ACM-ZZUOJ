#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

from math import sqrt

d = input().split()
a = float(d[0])
b = int(d[1])
c = int(d[2])
p = (a + b + c)/2
S = sqrt(p*(p-a)*(p-b)*(p-c))
print("%0.2f"%S)
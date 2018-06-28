#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

PI = 3.14159

a = input().split()
r = float(a[0])
h = float(a[1])
#底圆周长
d = 2 * PI * r
s = PI * r**2 * 2 + d * h
print("%0.2f"% s)
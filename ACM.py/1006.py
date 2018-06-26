#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

a = input().split()
a1 = int(a[0])
a2 = int(a[1])
a3 = int(a[2])

S = (a1 + a2)/2 * ((a2 - a1)/a3 + 1)
print(int(S))

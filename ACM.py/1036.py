#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

a = input().split()
b1 = [1, 3, 5, 7, 8, 10, 12]
b2 = [4, 6, 9, 11]
a1 = int(a[0])
a2 = int(a[1])
if a2 in b1:
    print(31)
elif a2 in b2:
    print(30)
else:
    if (a1%100 ==0 and a1%400 == 0) or (a1%100 != 0 and a1%4 == 0):
        print(29)
    else:
        print(28)




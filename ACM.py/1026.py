#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

a = input()
m = ord(a)
if ord('a') < m and m < ord('z'):
    print("lower")
elif ord('A') < m and m < ord('Z'):
    print("upper")
elif 18 <= m and m <=59:
    print("digit")
else:
    print("other")


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

a = input()
b = input()

s1 = a.split(":")
s2 = b.split(":")

a1 = (int(s2[0]) - int(s1[0])) * 3600
a2 = (int(s2[1]) - int(s1[1])) * 60
a3 = int(s2[2]) - int(s1[2])

print(a1+a2+a3)



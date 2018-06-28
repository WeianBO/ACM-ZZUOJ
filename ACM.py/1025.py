#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

# a = input().split()
# a.sort()
# print(a[-1])

a = input().split()
m = 0
for i in a:
    if ord(i) > m:
        m = ord(i)
    else:
        continue
print(chr(m))


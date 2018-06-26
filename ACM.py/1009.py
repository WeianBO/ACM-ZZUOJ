#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

r = input().split()
c = 0
for m in r:
    c = c + int(m)
print("%0.2f"% (c/3))

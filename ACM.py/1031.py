#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

a = input().split()

a1 = int(a[0])
a2 = int(a[1])

def quadrant():
    if a1 > 0 and a2 > 0:
        print(1)
    elif a1 < 0 and a2 > 0:
        print(2)
    elif a1 < 0 and a2 < 0:
        print(3)
    else:
        print(4)

if __name__ == "__main__":
    quadrant()


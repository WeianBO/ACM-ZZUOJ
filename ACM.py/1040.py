#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

a = int(input())

def sum():
    s = 0
    for n in range(1, a+1):
        s = 1 / (2 * n - 1) + s
    print("%0.2f" % s)

if __name__ == "__main__":
    sum()

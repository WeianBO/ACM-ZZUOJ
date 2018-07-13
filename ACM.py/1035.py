#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

a = int(input())

def fun():
    if a <= -2:
        m = 7 - 2 * a
    elif a > -2 and a < 3:
        m = 5 - abs(3 * a + 2)
    else:
        m = a * 3 + 4
    print(m)

if __name__ == "__main__":
    fun()


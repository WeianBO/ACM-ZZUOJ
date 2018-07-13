#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

a = int(input())

def salary():
    if a <= 10000:
        m = a * 0.05 + 1500

    elif a > 10000 and a < 50000:
        m = 500 + (a - 10000) * 0.03 + 1500

    else:
        m = 1700 + (a - 50000) * 0.02 + 1500

    print(m)

if __name__ == "__main__":
    salary()
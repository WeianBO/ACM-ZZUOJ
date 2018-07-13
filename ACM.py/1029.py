#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

a = input().split()
a1 = int(a[0])
a2 = int(a[1])
a3 = int(a[2])

def trangle():
    if ((a1 + a2) > a3):
        if (abs(a1 - a2) < a3):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == "__main__":
    trangle()


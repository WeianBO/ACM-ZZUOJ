#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

n = int(input())
a = input().split()

def sum():
    s = 0
    for m in range(n):
        s = int(a[m]) + s
    print(s)

if __name__ == "__main__":
    sum()


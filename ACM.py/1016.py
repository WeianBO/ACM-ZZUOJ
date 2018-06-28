#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

a = input().split()
a1 = int(a[0])
deposit = int(a[1])

def money(deposit, a1):
    for i in range(a1):
        deposit = deposit * (1 + 2.25 / 100)
    print("%0.6f" % deposit)

if __name__ == "__main__":
    money(deposit, a1)



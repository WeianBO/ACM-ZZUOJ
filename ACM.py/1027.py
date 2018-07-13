#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

a = input()
a1 = int(a)
a2 = list(a)
def add_list():
    m = 0
    for i in a2:
        m = int(i)**3 + m
    return m

if a1 == add_list():
    print("yes")
else:
    print("no")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

a = int(input())
if a%100 ==0 and a%400 == 0:
    print("Yes")
elif a%100 != 0 and a%4 == 0:
    print("Yes")
else:
    print("No")
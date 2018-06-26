#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

'''
设鸡 ：a , 兔: b
n = 2a + 4b
m = a +b 

b = (n - 2*m)/2
'''

l = input().split()
m = int(l[0])
n = int(l[1])
b = (n - 2*m)/2
a = m - b
print(int(a), end=' ')
print(int(b))
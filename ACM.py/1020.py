#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

# sorted(list， reverse=False) 从小到大排序list 默认reverse=False
# list.sort() 也是排序，不过改变list本身

a = input().split()
b = sorted(a)
print("%d %d" % (int(b[0]), int(b[1])))



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

# reserve 用于反向列表中的数据
# sort 本身是从小到大排序

a = input().split()
a.sort(reverse=True)
for i in a:
    print(int(i), end=" ")
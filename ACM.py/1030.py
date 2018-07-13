#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'


a = input().split()
b = []
# a = sorted(a) 列表中的数字算作字符串，所以按开头的第一个字符
for m in a:
    b.append(int(m))
b.sort()
a1 = int(b[0])
a2 = int(b[1])
a3 = int(b[2])

def trangle():
    if a1**2 + a2**2 == a3**2:
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    trangle()






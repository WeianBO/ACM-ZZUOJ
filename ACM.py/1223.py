#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

name = list("snail")

group_num = int(input())
a = []
for i in range(group_num):
    s = input().lower()
    if len(s) <= 200:
        a.append(s)

def count(group):
    num = 0
    for i in name:
        num = group.count(i) + num
    per = num / len(group) *100
    print("%d%%"% per)

if __name__ == '__main__':
    for m in range(group_num):
        count(a[m])















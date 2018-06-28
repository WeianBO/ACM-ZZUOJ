#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

# string.uppercase 大写字母字符串
# # string.lowercase 小写字母字符串

import string

a = input()
# a = a.lower()
# s = []
#
# for i in string.ascii_lowercase:
#     s.append(i)
# print(s.index(a.lower())+1)

print(ord(a.lower()) - 96) #‘a’ 的ascii 码值是97  chr() 求数字对应字符
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'GonnaZero'

ticket = int(input())

if ticket < 30:
    print("%0.2f" % (ticket * 50))
else:
    print("%0.2f" % (ticket * 48))


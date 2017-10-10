#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/10 17:24
# @Author  : Mamba
# @Site    : 
# @File    : main.py


from utilize import *


if __name__ == '__main__':
    zi, mui = DataGenerator(N=1000, mu=1, sigma=1)
    Data2Bin(zi, bins=32)
    pass
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/10 16:57
# @Author  : Mamba
# @Site    : 
# @File    : utilize.py

import numpy as np
import pandas as pd


def DataGenerator(N, mu, sigma=1):
    mui = np.random.exponential(scale=mu, size=N)
    zi = np.apply_along_axis(np.random.normal, axis=0,
                             arr=mui, scale=sigma)
    return zi, mui


def getTweedieEst(zi, model="ns", degree=5, bins=32):

    pass


def Data2Bin(zi, bins):
    ziGroup = pd.qcut(zi, bins, labels=False)
    ziDf = pd.DataFrame(np.array(ziGroup.to_list(), zi), columns=['group', 'value'])
    ziDf.groupby(by='group')
    return


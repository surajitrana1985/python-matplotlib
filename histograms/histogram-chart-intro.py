#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:00:21 2021

@author: surajitrana
"""


import matplotlib.pyplot as plt
import numpy as np


def plot_histogram():
    x = np.random.normal(170, 10, 250)
    plt.hist(x, color="hotpink")
    plt.show()


if __name__ == '__main__':
    plot_histogram()

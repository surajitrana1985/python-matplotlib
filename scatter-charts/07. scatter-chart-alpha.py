#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:41:58 2021

@author: surajitrana
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_scatter():
    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
    sizes = np.array([20, 50, 100, 200, 500, 1000,
                     60, 90, 10, 300, 600, 800, 75])
    plt.scatter(x, y, sizes=sizes, alpha=0.5)
    plt.show()


if __name__ == '__main__':
    plot_scatter()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:24:57 2021

@author: surajitrana
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_scatter():
    #day one, the age and speed of 13 cars:
    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
    plt.scatter(x, y, color="hotpink")

    #day two, the age and speed of 15 cars:
    x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
    y = np.array([100, 105, 84, 105, 90, 99, 90,
                 95, 94, 100, 79, 112, 91, 80, 85])
    plt.scatter(x, y, color="green")

    plt.show()


if __name__ == '__main__':
    plot_scatter()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:32:53 2021

@author: surajitrana
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_scatter():
    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

    # Adding colorbar
    plt.scatter(x, y, c=colors, cmap="viridis")
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    plot_scatter()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:45:45 2021

@author: surajitrana
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_scatter():
    x = np.random.randint(100, size=(100))
    y = np.random.randint(100, size=(100))
    colors = np.random.randint(100, size=(100))
    sizes = 10 * np.random.randint(100, size=(100))

    plt.scatter(x, y, c=colors, cmap="nipy_spectral", sizes=sizes, alpha=0.5)
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    plot_scatter()

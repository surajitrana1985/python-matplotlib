#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 22:37:00 2021

@author: surajitrana
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    x_points = np.array([1, 2, 6, 8])
    y_points = np.array([3, 8, 1, 10])
    plt.plot(x_points, y_points, "o--m", markersize=14,
             mec="#000000", mfc="hotpink")
    plt.show()


if __name__ == "__main__":
    plot_graph()

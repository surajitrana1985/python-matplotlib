#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 21:15:14 2021

@author: surajitrana
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    x_points = np.array([0, 100])
    y_points = np.array([0, 1000])
    plt.plot(x_points, y_points)
    plt.show()


if __name__ == "__main__":
    plot_graph()

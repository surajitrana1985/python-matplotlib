#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:54:47 2021

@author: surajitrana
"""

import matplotlib.pyplot as plt
import numpy as np


plot_x_data = [
    [10, 30, 50, 80, 100],
    [50, 100, 150, 200, 250],
    [0, 100, 200, 300, 400],
    [10, 30, 50, 80, 100]
]

plot_y_data = [
    [100, 0, 50, 200, 0],
    [50, 90, 950, 100, 50],
    [0, 100, 1000, 10000, 100000],
    [900, 700, 500, 300, 100]
]

style_type = ["-", "--", "-.", ":"]

colors = ["r", "g", "b", "k"]

titles = ["SALES", "PRODUCTS", "CUSTOMERS", "FORECAST"]

markers = ["o", "X", "D", "s"]


def plot_graph():
    for i in range(4):
        x = np.array(plot_x_data[i])
        y = np.array(plot_y_data[i])
        plt.subplot(2, 2, i + 1)
        plt.plot(
            x, y, linestyle=style_type[i], color=colors[i], marker=markers[i], markersize=10)
        plt.title(titles[i])
        plt.subplots_adjust(top=1.5, bottom=0.2, left=0.2)
    plt.show()


if __name__ == '__main__':
    plot_graph()

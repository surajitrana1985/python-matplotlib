#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 23:02:28 2021

@author: surajitrana
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    x_series_1 = np.array([0, 400, 800, 1200, 1600])
    x_series_2 = np.array([5, 100, 200, 400, 700])
    x_series_3 = np.array([0, 500, 1000, 1500, 2000])
    y_series_1 = np.array([10, 0, 600, 678, 1000])
    y_series_2 = np.array([790, 670, 0, 300, 1000])
    y_series_3 = np.array([1000, 100, 89, 0, 700])
    plt.plot(x_series_1, y_series_1, linestyle=":",
             color="red", linewidth="3", marker="o")
    plt.plot(x_series_2, y_series_2, linestyle="--",
             color="green", linewidth="3", marker="X")
    plt.plot(x_series_3, y_series_3, linestyle="-.",
             color="blue", linewidth="3", marker="D")
    plt.show()


if __name__ == "__main__":
    plot_graph()

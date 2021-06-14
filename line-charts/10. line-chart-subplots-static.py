#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:15:14 2021

@author: surajitrana
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    # plot 1
    x = np.array([0, 1, 2, 3])
    y = np.array([3, 8, 1, 10])
    plt.subplot(1, 2, 1)
    plt.plot(x, y, color="green")
    plt.title("PRODUCT")
    plt.xlabel("Index")

    # plot 2
    x = np.array([1, 7, 10, 15])
    y = np.array([10, 100, 500, 0])
    plt.subplot(1, 2, 2)
    plt.plot(x, y, color="red")
    plt.title("SALES")
    plt.xlabel("Index")

    plt.subplots_adjust(top=0.8)
    plt.suptitle("Product vs Sales", fontsize="16",
                 fontweight="3")
    plt.show()


if __name__ == '__main__':
    plot_graph()

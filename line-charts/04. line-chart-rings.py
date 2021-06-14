#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 21:34:04 2021

@author: surajitrana
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    x_points = np.array(range(0, 1000, 50))
    y_points = np.array(range(0, 1000, 50))
    plt.plot(x_points, y_points, "o")
    plt.show()


if __name__ == "__main__":
    plot_graph()

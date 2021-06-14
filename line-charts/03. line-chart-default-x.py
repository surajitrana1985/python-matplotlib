#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 22:16:48 2021

@author: surajitrana
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    y_points = np.array([3, 8, 1, 10, 5, 7])
    plt.plot(y_points)
    plt.show()


if __name__ == "__main__":
    plot_graph()

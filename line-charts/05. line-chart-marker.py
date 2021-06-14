#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 22:21:10 2021

@author: surajitrana
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    y_series = np.array([10, 2, 99, 155, 4, 190])
    plt.plot(y_series, marker="o")
    plt.show()


if __name__ == '__main__':
    plot_graph()

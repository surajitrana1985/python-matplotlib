#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 21:46:25 2021

@author: surajitrana
"""

""" Draw a line in a diagram from position 
(1, 3) to (2, 8) then to (6, 1) and finally
to position (8, 10):
"""




import matplotlib.pyplot as plt
import numpy as np
def plot_graph():
    x_points = np.array([1, 2, 6, 8])
    y_points = np.array([3, 8, 1, 10])
    plt.plot(x_points, y_points)
    plt.show()


if __name__ == "__main__":
    plot_graph()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 20:10:07 2021

@author: surajitrana
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_chart():
    x_series = np.array(["May 01, 2021", "May 10, 2021",
                        "May 20, 2021", "May 29, 2021", "June 01, 2021"])
    y_series = np.array([120, 457, 897, 23, 0])

    # Creating font styles for title and axes labels
    fonttitle = {'family': 'arial', 'color': 'green', 'size': 20}
    fontx = {'family': 'serif', 'color': 'blue', 'size': 15}
    fonty = {'family': 'serif', 'color': 'darkred', 'size': 15}

    # Creating title and axes labels and assigning font styles
    plt.title("Total sales over a period of time (in millions)",
              fontdict=fonttitle, loc="left", pad="20")
    plt.xlabel("Timeline", fontdict=fontx)
    plt.ylabel("Total Sales", fontdict=fonty)

    # Adding grids to the plot
    plt.grid(axis="both", color="blue", linestyle="--", linewidth="1")

    plt.plot(x_series, y_series, linestyle="-.",
             color="hotpink", linewidth="3", marker="o")
    plt.show()


if __name__ == '__main__':
    plot_chart()

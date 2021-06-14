#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:29:29 2021

@author: surajitrana
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_piechart():
    dataset = np.array([20, 25, 10, 15, 30])
    chart_lables = np.array(["Audi", "Mercedez", "BMW", "Tesla", "Volvo"])
    chart_explode = [0.2, 0, 0, 0, 0]
    chart_colors = ["black", "hotpink", "c", "#4CAF50", "yellow"]
    plt.pie(dataset, labels=chart_lables, startangle=90,
            explode=chart_explode, shadow=True, colors=chart_colors)
    # Adding legend
    plt.legend(title="Best cars of 2020-21", loc="lower right")
    plt.show()


if __name__ == '__main__':
    plot_piechart()

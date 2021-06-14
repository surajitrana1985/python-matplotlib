#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:24:34 2021

@author: surajitrana
"""


import matplotlib.pyplot as plt
import numpy as np


def plot_piechart():
    dataset = np.array([20, 25, 10, 15, 30])
    chart_lables = np.array(["Audi", "Mercedez", "BMW", "Tesla", "Volvo"])
    chart_explode = [0.2, 0, 0, 0, 0]
    plt.pie(dataset, labels=chart_lables, startangle=90, explode=chart_explode)
    plt.show()


if __name__ == '__main__':
    plot_piechart()

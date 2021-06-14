#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:17:49 2021

@author: surajitrana
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_piechart():
    dataset = np.array([20, 25, 10, 15, 30])
    chart_lables = np.array(["Audi", "Mercedez", "BMW", "Tesla", "Volvo"])
    plt.pie(dataset, labels=chart_lables)
    plt.show()


if __name__ == '__main__':
    plot_piechart()

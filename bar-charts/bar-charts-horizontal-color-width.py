#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:51:33 2021

@author: surajitrana
"""


import matplotlib.pyplot as plt
import numpy as np


def plot_barchart():
    x = np.array(["Apple", "Samsung", "IBM", "Intel"])
    y = np.array([1000, 560, 900, 678])

    plt.xlabel("Brands")
    plt.ylabel("Sales (in billions USD)")
    plt.title("Sales of brands over FY1-2021")
    plt.barh(x, y, color="green", height=0.2)
    plt.show()


if __name__ == '__main__':
    plot_barchart()

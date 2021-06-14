"""
Created on Mon Jun 14 13:17:49 2021

@author: surajitrana
"""


import matplotlib.pyplot as plt
import numpy as np


def plot_piechart():
    dataset = np.array([30, 5, 20, 45])
    plt.pie(dataset)
    plt.show()


if __name__ == '__main__':
    plot_piechart()

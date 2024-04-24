#!/usr/bin/python3
"""
commentttttttttttttttttttttttt
"""
import math


def pascal_triangle(n):
    """ commentttttttttttttttttttttttt """
    ls = []
    if n <= 0:
        return []
    for i in range(1, n + 1):
        ls.append([])
        for j in range(0, i):
            ls[i - 1].append(math.comb(i - 1, j))
    return ls

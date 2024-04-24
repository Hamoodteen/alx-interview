#!/usr/bin/python3
"""
commentttttttttttttttttttttttt
"""


def factorial(n):
    """ commentttttttttttttttttttttttt """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def combination(n, r):
    """ commentttttttttttttttttttttttt """
    return factorial(n) // (factorial(r) * factorial(n - r))


def pascal_triangle(n):
    """ commentttttttttttttttttttttttt """
    ls = []
    if n <= 0:
        return []
    for i in range(1, n + 1):
        ls.append([])
        for j in range(0, i):
            ls[i - 1].append(combination(i - 1, j))
    return ls

#!/usr/bin/python3
"""12-pascal_triangle.py"""


def pascal_triangle(n):
    """pascal_triangle
    Args:
        n (int): number of rows
    Returns:
        list: list of lists of integers
    """
    if n <= 0:
        return []
    Pt = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(Pt[i - 1][j - 1] + Pt[i - 1][j])
        row.append(1)
        Pt.append(row)
    return Pt

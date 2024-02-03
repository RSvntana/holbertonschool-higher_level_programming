#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        matrix: matrix to divide
        div: divisor
    Returns:
        new matrix
    Raises:
        TypeError: if matrix is not a list of lists of integers or floats
        TypeError: if matrix contains rows of different sizes
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0

    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], -2)
    [[-0.5, -1.0, -1.5], [-2.0, -2.5, -3.0]]
    >>> matrix_divided([[1.5, 2.8, 3.3], [4.2, 5.5, 6.6]], 2)
    [[0.75, 1.4, 1.65], [2.1, 2.75, 3.3]]
    """
    if type(matrix) is not list\
            or not all(type(row) is list for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(type(num) in [int, float] for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(set(map(len, matrix))) > 1:
        raise ValueError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    def div_matrix(x, div): return round(x / div, 2)
    new_matrix = [[div_matrix(num, div) for num in row] for row in matrix]
    return new_matrix

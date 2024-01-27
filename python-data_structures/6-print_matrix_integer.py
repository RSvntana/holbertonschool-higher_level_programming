#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        if row == []:
            print("")
        else:
            for i, element in enumerate(row):
                if i < len(row) - 1:
                    print("{:d}".format(element), end=" ")
                else:
                    print("{:d}".format(element))

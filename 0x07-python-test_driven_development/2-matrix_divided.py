#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """define parameter to divides"""
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError("matrix
                        must be a matrix (list of lists) of integers/floats")

    if type(div) != (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    if type(matrix[0]) != list:
        raise TypeError("matrix
                        must be a matrix (list of lists) of integers/floats")

    matrilen = len(matrix[0])
    newmatrix = []
    for matri in matrix:
        if type(matri) != list:
            raise TypeError("matrix
                        must be a matrix (list of lists) of integers/floats")
        if len(matri) != matrilen:
            raise TypeError("Each row of the matrix must have the same size")
        newmatri = []
        for i in matri:
            if type(i) != int and type(i) != float:
                raise TypeError("matrix
                        must be a matrix (list of lists) of integers/floats")
            newmatri.append(round(float(i / div), 2))
        newmatrix.append(newmatri)
    return newmatrix

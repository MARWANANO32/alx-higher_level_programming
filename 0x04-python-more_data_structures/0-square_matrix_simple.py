#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """the function that computes the square value of all integers of a matrix"""
    new_matrix = [x, y]
    for i in matrix:
        result = list(map(lambda x, y : x*x, y*y, i))
        new_matrix.append(result)
    return new_matrix

#!/usr/bin/python3
"""Module 12-pascal_triangle
Defines a function that returns Pascal's triangle
"""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]  # première ligne

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # premier élément
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # dernier élément
        triangle.append(row)

    return triangle

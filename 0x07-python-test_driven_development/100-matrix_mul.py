#!/usr/bin/python3
"""
This module contains only one function
matrix_mul(m_a, m_b), that multiplies 2 matrix
"""


def matrix_mul(m_a, m_b):
    """
    matrix_mul(m_a, m_b):
        matrix_mul takes two List of Lists and multiplies
        them in `Doted product (M1 . M2)`
        and return the result new_matrix

    Args:
       m_a: List of Lists of integers or floats
       m_b: List of Lists of integers or floats

    Return:
       m_a . m_b
    """
    new_matrix = []
    temp = []
    m_aR = 0
    m_aC = -1
    not_int_a = 0
    m_bR = 0
    m_bC = -1
    not_int_b = 0
    result = 0

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if not_int_a == 0:
            for i in row:
                if type(i) not in [int, float]:
                    not_int_a = 1
                    break
        m_aR += 1
        if m_aC == -1:
            m_aC = len(row)
        elif m_aC != len(row):
            m_aC = -2

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if not_int_b == 0:
            for i in row:
                if type(i) not in [int, float]:
                    not_int_b = 1
                    break
        m_bR += 1
        if m_bC == -1:
            m_bC = len(row)
        elif m_bC != len(row):
            m_bC = -2

    if len(m_a) == 0 or m_aC == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or m_bC == 0:
        raise ValueError("m_b can't be empty")

    if not_int_a == 1:
        raise TypeError("m_a should contain only integers or floats")
    if not_int_b == 1:
        raise TypeError("m_b should contain only integers or floats")

    if m_aC == -2:
        raise TypeError("each row of m_a must be of the same size")
    if m_bC == -2:
        raise TypeError("each row of m_b must be of the same size")
    if m_aC != m_bR:
        raise ValueError("m_a and m_b can't be multiplied")

    k = 0
    for i in range(m_aR):
        for _ in range(m_bC):
            for j in range(m_bR):
                result += m_a[i][j] * m_b[j][k]
            k += 1
            temp.append(result)
            result = 0
        new_matrix.append(temp)
        temp = []
        k = 0
    return new_matrix

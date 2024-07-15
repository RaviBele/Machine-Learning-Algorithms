import numpy as np
def sparse_matrix_multiplication(matrix_a, matrix_b):
    try:
        return np.dot(np.array(matrix_a), np.array(matrix_b)).tolist()
    except ValueError:
        return [[]]
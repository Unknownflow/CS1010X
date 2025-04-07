# Question 3
# Ordered Matrix

# Implement a function check_matrix(matrix) that reads in an N*M matrix implemented using nested tuples, checks whether all values in this matrix, according to row-major order, are in non-decreasing order. If the matrix is in the right order, return True, else, return False.

#     Matrix values in sample run #1 below can be read as -1, 2, 3, 4, 5, 6, which is in non-decreasing order.
#     Matrix values in sample run #2 below can be read as -1, 2, 4, 3, 5, 6, which is not in non-decreasing order.

# You may assume that you will not be given an empty matrix

def check_matrix(matrix):

    prev = -10000000000000000000000

    for i in range(len(matrix)):

        for j in range(len(matrix[0])):

            if matrix[i][j] >= prev:

                prev = matrix[i][j]

            else:

                return False

    return True
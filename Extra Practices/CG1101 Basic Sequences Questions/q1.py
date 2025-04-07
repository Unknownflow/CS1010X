# Question 1

#Easy Sudoku

#Sudoku is a logic-based, combinatorial number-placement puzzle where the objective is to fill in a 9x9 grid.The rules of the game are:

#    Each column contains the digits from 1 to 9 only one time each.
#    Each row contains the digits from 1 to 9 only one time each.
#    Each 3x3 boxes contains the digits from 1 to 9 only one time each.

#In this problem, you are given a partially completed grid in a tuple of tuples as follows. We will use this data for all test cases.

#5 3 4  6 7 8  9 1 2
#6 0 2  1 9 0  3 4 0
#1 9 8  3 4 2  0 6 7

#8 5 9  7 6 1  4 2 3
#4 2 0  8 5 3  7 9 1
#7 1 3  9 2 4  8 5 6

#9 6 1  0 3 7  2 8 4
#2 8 7  4 1 9  6 0 5
#3 4 5  2 8 6  1 7 9

#To simplify your task, we will dismiss the last rule specified above. In our simplified Sudoku, we will only consider the following two rules:

#    Each column contains digits from 1 to 9 only one time each AND
#    Each row contains digits from 1 to 9 only one time each.

#In the provided grid, the incomplete slots are represented by 0. Write a program that accepts three integer inputs x y n, determine if value n at coordinate (x, y) will violate the two rules specified above or not. x is the line index starting from 1 whereby line 1 (the first line) is the topmost line; y is the column index starting from 1 whereby column 1 (the first column) is the leftmost column. Your program should return "No violation" if no rule is violated or return "Violation" if either rule is violated.

#For example if the input is 2 2 7, you should output "No violation" because putting value 7 in slot (2, 2) still ensures that each row and column only contains 1 to 9 only once. However if the input is 2 6 8, you should output "Violation" because putting value 8 in slot (2, 6) would result in digit 8 occurring twice on the 6th column.

#You may assume that (x, y) will always point to an undetermined slot (i.e., with value 0 in the grid).

#The grid and skeleton program are provided below.


SIZE = 9

board = ((5, 3, 4, 6, 7, 8, 9, 1, 2),

(6, 0, 2, 1, 9, 0, 3, 4, 0),

(1, 9, 8, 3, 4, 2, 0, 6, 7),

(8, 5, 9, 7, 6, 1, 4, 2, 3),

(4, 2, 0, 8, 5, 3, 7, 9, 1),

(7, 1, 3, 9, 2, 4, 8, 5, 6),

(9, 6, 1, 0, 3, 7, 2, 8, 4),

(2, 8, 7, 4, 1, 9, 6, 0, 5),

(3, 4, 5, 2, 8, 6, 1, 7, 9))

def easy_sudoku(x, y, n):

    x = x - 1

    y = y - 1

    row_values = []

    col_values = []

    for i in range(SIZE):

        if board[x][i] not in row_values and board[x][i] != n:

            if board[x][i] != 0:

                 row_values.append(board[x][i])

        else:

            return 'Violation'

       

        if board[i][y] not in col_values and board[i][y] != n:

            if board[i][y] != 0:

                col_values.append(board[i][y])

        else:

            return 'Violation'

    

    return 'No violation'

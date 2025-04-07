#Question 1

#Filling Rows

#The first step in our algorithm is to check for 0s in each row of the board, and if only a single 0 is found, we replace it with the missing digit in the row.

#Write a function fill_row(board) that takes in a board, which is a lists of lists, and inserts the missing digit in each row with a single 0. The function should return True if any digit was inserted and False otherwise.

SIZE = 4

board1 = [[1, 0, 3, 0], [3, 0, 0, 2], [4, 3, 2, 1], [0, 0, 0, 3]]

board2 = [[0, 1, 3, 2], [2, 0, 1, 0], [1, 0, 0, 3], [3, 4, 2, 1]]

board3 = [[0, 0, 0, 0], [0, 1, 2, 4], [0, 3, 4, 1], [0, 4, 0, 2]]

def fill_row(board):

    filled = False

    

    for i in range(len(board)):

        row = board[i]

        zero_pos = []

        non_zero_num = []

        

        for num in row:

            if num == 0:

                zero_pos.append(num)

            else:

                non_zero_num.append(num)

            

        if len(zero_pos) == 1:

            filled = True

            pos = zero_pos[0]

            for j in range(1, 5):

                if j not in non_zero_num:

                    board[i][pos] = j

    if filled:

        return True

    else:

        return False

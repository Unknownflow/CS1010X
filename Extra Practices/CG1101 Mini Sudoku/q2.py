#Question 2

#Filling Columns

#The second step of our algorithm is to go through each column, finding columns with single zeros and filling them up with the missing digit.

#Write a function fill_col(board) that takes in the same type of board as before, and inserts the missing digit for columns with only a single zero.

#The return value should be True if a digit was inserted and False otherwise.

#The fill_row function previously defined is available too.

def fill_col(board):

    filled = False

    

    for i in range(len(board)):

        row = board[i]

        zero_pos = []

        non_zero_num = []

        

        for j in range(len(board)):

            if board[j][i] == 0:

                zero_pos.append(j)

            else:

                non_zero_num.append(board[j][i])

            

        if len(zero_pos) == 1:

            filled = True

            pos = zero_pos[0]

            for j in range(1, 5):

                if j not in non_zero_num:

                    board[pos][i] = j

    if filled:

        return True

    else:

        return False

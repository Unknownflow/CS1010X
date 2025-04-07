#Question 3

#Filling Sections

#The third step of the algorithm is to go through each of the 2x2 sections in the grid and fill in the sections a single missing digit.

#Write a function called fill_section(board) that takes in a board like before and inserts the missing digit for sections with only a single 0.

#The function should return True if a digit was inserted and False otherwise.

#You may make use of the fill_row and fill_col functions.


def fill_section(board):

    filled = False

    indexArr = [[[0,0], [0,1], [1,0], [1,1]],

             [[2,0], [3,0], [2,1], [3,1]],

             [[0,2], [0,3], [1,2], [1,3]],

             [[2,2], [2,3], [3,2], [3,3]]]

    for indexSubArr in indexArr:

        zero_pos = []

        non_zero_num = []

        

        for index in indexSubArr:

            i, j = index

            if board[i][j] == 0:

                zero_pos.append(index)

            else:

                non_zero_num.append(board[i][j])

        if len(zero_pos) == 1:

            filled = True

            i, j = zero_pos[0]

            for k in range(1, 5):

                if k not in non_zero_num:

                    board[i][j] = k

    if filled:

        return True

    else:

        return False

#Question 3

#Filling the Board

#Now that we've nailed down the 3 repeated steps of the algorithm, all we have to do is apply these steps until no more 0s can be found in the grid.

#Define a function fill_board(board) that repeatedly applies the 3 steps of the algorithm until no more 0s can be found.

#The function should return the given board when done.

#Note that fill_row, fill_col and fill_section have already been defined as described in previous questions. You can just simply call them!



def fill_board(board):

    fillable = True  # indicate if a board is still fillable

    # if still fillable, you shall continue filling it

    # if no longer fillable, shall return the board

    while fillable:

        fill_row_bool = fill_row(board)

        fill_col_bool = fill_col(board)

        fill_sec_bool = fill_section(board)

        print(fill_row_bool, fill_col_bool, fill_sec_bool)

        print(board)

        if not fill_sec_bool:

            fillable = False

            

    # write your code here

    return board

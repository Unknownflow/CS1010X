#
# CS1010X --- Programming Methodology
#
# Sidequest 10.1 Template
#
# Note that written answers are commented out to allow us to run your #
# code easily while grading your problem set.

from random import *
from puzzle import GameGrid

###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]



###########
# Task 1  #
###########

def new_game_matrix(n):
    """create an empty square matrix of size n"""
    matrix = [[0 for i in range(n)] for i in range(n)]
    return matrix

# print(new_game_matrix(5))

def has_zero(mat):
    """returns true if matrix has an entry value of 0, false otherwise"""
    flatten_mat = flatten(mat)
    return 0 in flatten_mat

# print(has_zero([[2,2],[2,2]]))
# print(has_zero([[2,0],[0,2]]))


def add_two(mat):
    """create 2 at a random location in matrix if possible"""
    if not has_zero(mat): # no zero location found, return original matrix
        return mat
    else:
        zero_count = 0
        zeroes_dict = {}

        for i in range(len(mat)):
            for j in range(len(mat)):
                # get all 0 location and input it into a dict
                if mat[i][j] == 0:
                    zeroes_dict[zero_count] = (i, j)
                    zero_count += 1

        # choose a random zero and replace that 0 with a 2
        random_zero = randint(0, zero_count-1)
        row, col = zeroes_dict[random_zero]
        mat[row][col] = 2
        return mat
        
# print(add_two([[4,8],[16,0]]))
# print(add_two([[0,0],[0,0]]))


###########
# Task 2  #
###########

def game_status(mat):
    """check game status whether the game has ended"""
    def possible_moves(mat):
        """check if there are possible moves in the matrix"""
        for i in range(len(mat)):
            for j in range(1, len(mat)):
                # if number is same as number in prev col or prev row, there are possible moves
                if mat[j][i] == mat[j-1][i] or \
                  mat[i][j] == mat[i][j-1]:
                    return True
        return False
    
    flatten_mat = flatten(mat)
    if 2048 in flatten_mat: # 2048 tile created
        return 'win'
    
    # no possible moves and no empty tiles, hence game is lost
    if not possible_moves(mat) and not has_zero(mat):
        return 'lose'
    
    # otherwise, game is not over
    return 'not over'
    
    

# print(possible_moves([[1,2,3], [4,5,6], [7,8,9]])) # f
# print(possible_moves([[2,2,3], [4,5,6], [7,8,9]])) # t
# print(possible_moves([[1,2,2], [4,5,6], [7,8,9]])) # t
# print(possible_moves([[1,2,1], [4,5,6], [7,8,9]])) # f
# print(possible_moves([[1,2,3], [1,5,6], [7,8,9]])) # t
# print(possible_moves([[1,2,3], [4,2,6], [7,8,9]])) # t
# print(possible_moves([[1,2,3], [4,5,3], [7,8,9]])) # t
# print(possible_moves([[1,2,9], [4,5,6], [7,8,9]])) # f
# print(possible_moves([[1,8,3], [4,5,6], [7,8,9]])) # f
# print(possible_moves([[7,2,3], [4,5,6], [7,8,9]])) # f
# print(possible_moves([[1,2,3], [4,5,6], [7,8,9]]))

# print(game_status([[2, 0, 2, 2], [0, 0, 0, 4], [4, 0, 8, 4], [2, 0, 0, 2048]]))
# print(game_status([[2, 0, 2, 4], [0, 2, 4, 2], [2, 4, 0, 4], [4, 2, 4, 0]]))
# print(game_status([[2, 4, 16, 4], [4, 2, 2, 2], [2, 4, 2, 4], [4, 2, 4, 8]]))
# print(game_status([[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]]))

###########
# Task 3a #
###########

def transpose(mat):
    transposed_matrix = [[row[i] for row in mat] for i in range(len(mat[0]))]
    matrix_len = len(mat)
    transposed_len = len(transposed_matrix)

    for i in range(matrix_len, transposed_len):
        mat.append([])

    for i in range(transposed_len, matrix_len):
        mat.pop()

    for i in range(transposed_len):
        mat[i] = transposed_matrix[i]

    return mat



###########
# Task 3b #
###########

def reverse(mat):
    new_mat = []

    for arr in mat:
        reversed_arr = arr[::-1]
        new_mat.append(reversed_arr)
    
    return new_mat

# print(reverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

############
# Task 3ci #
############

matrix1 = [[2, 2, 0, 2], [4, 0, 0, 0], [4, 8, 0, 4], [0, 0, 0, 2]]
matrix2 = [[2,2], [0,0]]
matrix3 = [[2,0], [0,0]]

# todo
def merge_left(mat):
    def merge(row):
        new_row = []
        curr_tile = None
        score = 0

        for next_tile in row:
            if next_tile == 0: # skip 0s
                continue
            if next_tile == curr_tile: # CurrTile == NextTile => add tile of combined val to leftmost cell
                new_row.append(curr_tile * 2)
                score += curr_tile * 2
                curr_tile = None
            elif curr_tile and next_tile != curr_tile: # CurrTile != NextTile => add CurrTile to leftmost cell
                new_row.append(curr_tile)
                curr_tile = next_tile
            elif not curr_tile:
                curr_tile = next_tile
        
        # dont append None
        if curr_tile:
            new_row.append(curr_tile)

        # add 0s to the remaining tiles which are not merged
        for i in range(len(new_row), len(row)):
            new_row.append(0)
        
        if row == new_row:
            is_valid = False
        else:
            is_valid = True

        return new_row, is_valid, score

    result = list(map(lambda x: merge(x), mat))
    score_increment = 0
    is_valid = False
    new_matrix = []
    
    # result is a list of new_row, is_valid, score
    for item in result:
        new_matrix.append(item[0])
        score_increment += item[2]

        if item[1]: # this is is_valid
            is_valid = True

    return new_matrix, is_valid, score_increment


# print('a',merge([2,0,2,4]))
# print('a',merge([2,0,4,0]))
# print('a',merge([2,2,4,4]))

# print(merge_left([[2, 2, 0, 2], [4, 0, 0, 0], [4, 8, 0, 4], [0, 0, 0, 2]]))

# print(merge_left([[2,2], [0,0]]))

# print(merge_left([[2,0], [0,0]]))

#############
# Task 3cii #
#############

def merge_right(mat):
    # need to reverse the matrix to use merge left and need to reverse it back after 
    reversed_mat = reverse(mat)
    new_matrix, is_valid, score_increment = merge_left(reversed_mat)
    new_matrix = reverse(new_matrix)

    return new_matrix, is_valid, score_increment

# print(matrix1)
# print(transpose(matrix1))
# print(matrix2)
# print(transpose(matrix2))

def merge_up(mat):
    transposed_mat = transpose(mat)
    new_matrix, is_valid, score_increment = merge_left(transposed_mat)
    new_matrix = transpose(new_matrix)
    
    return new_matrix, is_valid, score_increment

# print(merge_left(matrix1))
# print(matrix1)
# print(merge_up(matrix1))
# print(matrix2)
# print(merge_up(matrix2))
# print(matrix3)
# print(merge_up(matrix3))

def merge_down(mat):
    # to get to merge_left pos, need to reverse, transpose then reverse again
    transposed_mat = reverse(transpose(reverse(mat)))
    new_matrix, is_valid, score_increment = merge_left(transposed_mat)
    new_matrix = reverse(transpose(reverse(new_matrix)))
    
    return new_matrix, is_valid, score_increment


###########
# Task 3d #
###########

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return

# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
# text_play()


# How would you test that the winning condition works?
# Your answer:
# I will check if the player wins when the tile 2048 is created
#


##########
# Task 4 #
##########

def make_state(matrix, total_score):
    return (matrix, total_score)

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def make_new_game(n):
    mat = new_game_matrix(n)
    for i in range(2):
        add_two(mat)
    return make_state(mat, 0) 

def moves(direction_function, state):
    mat = get_matrix(state)
    score = get_score(state)
    new_matrix, is_valid, score_increment = direction_function(mat)
    new_score = score + score_increment

    # randomly create 2 on the board if valid move is made
    if is_valid:
        add_two(new_matrix)

    new_state = make_state(new_matrix, new_score)
    return new_state, is_valid

def left(state):
    return moves(merge_left, state)

def right(state):
    return moves(merge_right, state)

def up(state):
    return moves(merge_up, state)

def down(state):
    return moves(merge_down, state)


# Do not edit this #
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': lambda state: (state, False)
}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
# gamegrid = GameGrid(game_logic)




#################
# Optional Task #
#################
 
consecutive_undo = 0

###########
# Task 5i #
###########

def make_new_record(mat, increment):
    return (mat, increment)

def get_record_matrix(record):
    return record[0]

def get_record_increment(record):
    return record[1]

############
# Task 5ii #
############

def make_new_records():
    return []

def push_record(new_record, stack_of_records):
    if len(stack_of_records) < 3:
        stack_of_records.append(new_record)
        return stack_of_records
    else:
        # clear the stack and add the top 2 element of the stack into the stack, with the new record
        first_mat, first_increment, first_stack_records = pop_record(stack_of_records)
        second_mat, second_increment, second_stack_records = pop_record(stack_of_records)        
        pop_record(stack_of_records)        

        first_record = make_new_record(first_mat, first_increment)
        second_record = make_new_record(second_mat, second_increment)

        push_record(second_record, stack_of_records)
        push_record(first_record, stack_of_records)
        push_record(new_record, stack_of_records)
        return stack_of_records


    
def is_empty(stack_of_records):
    if len(stack_of_records) == 0:
        return True
    else:
        return False

def pop_record(stack_of_records):
    if is_empty(stack_of_records):
        return (None, None, stack_of_records)
    
    record_popped = stack_of_records.pop()
    mat = get_record_matrix(record_popped)
    increment = get_record_increment(record_popped)
    return (mat,) + (increment,) + (stack_of_records, )


#############
# Task 5iii #
#############

# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    return (matrix, total_score, records)

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def make_new_game(n):
    mat = new_game_matrix(n)
    add_two(mat)
    add_two(mat)
    return make_state(mat, 0, [])

def moves(direction_function, state):
    global consecutive_undo
    consecutive_undo = 0
    mat = get_matrix(state)
    score = get_score(state)
    new_matrix, is_valid, score_increment = direction_function(mat)
    new_score = score + score_increment

    # randomly create 2 on the board if valid move is made
    if is_valid:
        add_two(new_matrix)
        records = get_records(state)
        new_state = make_state(new_matrix, new_score, records)
        new_record = make_new_record(mat, score_increment)
        push_record(new_record, records)
    else:
        new_state = state

    return new_state, is_valid

def left(state):
    return moves(merge_left, state)

def right(state):
    return moves(merge_right, state)

def up(state):
    return moves(merge_up, state)

def down(state):
    return moves(merge_down, state)

# NEW FUNCTIONS TO DEFINE
def get_records(state):
    return state[2]

def undo(state):
    global consecutive_undo
    records = get_records(state)

    if is_empty(records) or consecutive_undo > 3:
        return (state, False)
    consecutive_undo += 1

    last_mat, last_score_increment, updated_stack = pop_record(records)
    total_score = get_score(state)

    if last_score_increment is not None:
        total_score -= last_score_increment

    if last_mat is None:
        last_mat = get_matrix(state)

    new_state = make_state(last_mat, total_score, records)
    return (new_state, True)



# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
game_logic = {
   'make_new_game': make_new_game,
   'game_status': game_status,
   'get_score': get_score,
   'get_matrix': get_matrix,
   'up': up,
   'down': down,
   'left': left,
   'right': right,
   'undo': undo
}
gamegrid = GameGrid(game_logic)

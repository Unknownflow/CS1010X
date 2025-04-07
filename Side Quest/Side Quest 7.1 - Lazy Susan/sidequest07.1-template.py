#
# CS1010X --- Programming Methodology
#
# Mission 7 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from lazy_susan import *

##########
# Task 1 #
##########

def solve_trivial_2(table):
    table_state = get_table_state(table)
    moves = tuple()

    for state in table_state:
        if state == 0:
            moves += (0, )
        else:
            moves += (1, )

    flip_coins(table, moves)
    return table


# test:
t2_1 = create_table(2)
solve_trivial_2(t2_1)
print(check_solved(t2_1))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t2_1_run = create_table(2)
# run(t2_1_run, solve_trivial_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_1_susan = create_table(2)
# Susan(t2_1_susan)

########################################################





##########
# Task 2 #
##########

def solve_trivial_4(table):
    table_state = get_table_state(table)
    moves = tuple()

    for state in table_state:
        if state == 0:
            moves += (0, )
        else:
            moves += (1, )
            
    flip_coins(table, moves)
    return table

# test:
t4_2 = create_table(4)
solve_trivial_4(t4_2)
print(check_solved(t4_2))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t4_2_run = create_table(4)
# run(t4_2_run, solve_trivial_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_2_susan = create_table(4)
# Susan(t4_2_susan)

########################################################





##########
# Task 3 #
##########

def solve_2(table):
    if check_solved(table):
        return table
    else:
        return flip_coins(table, (1, 0))

# test:
t2_3 = create_table(2)
solve_2(t2_3)
print(check_solved(t2_3))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t2_3_run = create_table(2)
# run(t2_3_run, solve_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_3_susan = create_table(2)
# Susan(t2_3_susan)

########################################################





##########
# Task 4 #
##########

def solve_4(table):
    moves = {
        'A': (1, 0, 1, 0),
        'B': (1, 1, 0, 0),
        'C': (1, 0, 0, 0)
    }
    moves_list = ('A', 'B', 'A', 'C', 'A', 'B', 'A')

    if check_solved(table):
        return table
    
    for i in range(7):
        move = moves_list[i]
        flips = moves[move]
        flip_coins(table, flips)
        
        if check_solved(table):
            return table


# test:
t4_4 = create_table(4)
solve_4(t4_4)
print(check_solved(t4_4))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t4_4_run = create_table(4)
# run(t4_4_run, solve_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_4_susan = create_table(4)
# Susan(t4_4_susan)

########################################################





##########
# Task 5 #
##########

def solve(table):
    size = get_table_size(table)

    # check if table is solved
    if check_solved(table):
        return table
    
    # base case where size of table is 2
    if size == 2:
        flip_coins(table, (1, 0))
        return table

    moves = {
        1: (1, 0, 1, 0),
        2: (1, 1, 0, 0),
        3: (1, 0, 0, 0)
    }
    
    prev_power = 1
    power = 2

    # generate the set of moves
    for i in range(4, size):
        if i == 2 ** power: 
            # for every 2**power, first half will be 1s and second half will be 0s
            moves[i] = tuple(1 for i in range(2**power)) + \
                       tuple(0 for i in range(2**power))
            
            # need to increment power as the current power is found alr
            power += 1
            prev_power += 1
        else:
            idx = i - 2 ** (prev_power) # find the correct index to copy from
            moves[i] = moves[idx] + tuple(0 for i in range(2**prev_power)) # first half is copied, second half is 0s
            moves[idx] = moves[idx] + moves[idx] # arr at orig idx repeats itself

    moves_list = (1, 2, 1, 3, 1, 2, 1)
    next_move = 4

    # pattern found is move_list + highest possible move + move_list
    for i in range(size-4):
        moves_list = moves_list + (next_move, ) + moves_list
        next_move += 1
    
    # do moves_list with moves from the moves dict, if solved, return table
    for i in range(len(moves_list)):
        move = moves_list[i]
        flips = moves[move]
        flip_coins(table, flips)

        if check_solved(table):
            return table

# test:
t2_5 = create_table(2)
solve(t2_5)
print(check_solved(t2_5))

t4_5 = create_table(4)
solve(t4_5)
print(check_solved(t4_5))

t8_5 = create_table(8)
solve(t8_5)
print(check_solved(t8_5))

t16_5 = create_table(16)
solve(t16_5)
print(check_solved(t16_5))

# Note: It is not advisable to execute run() if the table is large.

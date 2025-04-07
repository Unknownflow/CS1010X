#
# CS1010X --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########

def egyptian(function, n):
    # Fill in code here
    j = n - 2 # j denotes the side vertical length not inclusive of top and bottom
    k = n - 1 # k denotes max length - 1
    # rotate left to make one col of n patterns horizontal
    n_horizontal = quarter_turn_left(stackn(n, function))
    # rotate left to make one col of n - 2 patterns horizontal
    j_horizontal = quarter_turn_left(stackn(j, quarter_turn_right(function)))

    
    center = quarter_turn_left(stack_frac(
        1/n,
        j_horizontal,
        stack_frac(
            j/k,
            function,
            j_horizontal,
            )
        ))

    return quarter_turn_right(stack_frac(
        1/n,
        n_horizontal,
        stack_frac(
            j/k,
            center,
            n_horizontal,
            )
        ))

    
# Test
#show(egyptian(make_cross(rcross_bb), 5))
#show(egyptian(make_cross(rcross_bb),9))
show(egyptian(nova_bb, 9))

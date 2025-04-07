#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.
'''
def fractal(rune, n):
    # Fill in code here
    # base case where n is 1
    if n == 1:
        return rune
    else:
        return beside(stackn(2, fractal(rune, n-1)),

                      stack(
                          rune,
                          stackn(2, fractal(rune, n-1))
                          )
                      )


def dual_fractal(rune1, rune2, n):
    # Fill in code here
    if n == 1:
        return rune1
    else:
        return beside(rune1, stackn(2, dual_fractal(rune2, rune1, n-1)))

    
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

#show(<your rune>)
#show(egyptian(rcross_bb, 4))
#show(egyptian(egyptian(nova_bb, 4), 10))

show(egyptian(make_cross(corner_bb), 4)
     )
'''

def runeception(function):
    result = function
    
    for i in range(2,25):
        n = i * i
        
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
                result,
                j_horizontal,
                )
            ))
        

        result = quarter_turn_right(stack_frac(
            1/n,
            n_horizontal,
            stack_frac(
                j/k,
                center,
                n_horizontal,
                )
            ))

    return result



show(runeception(make_cross(rcross_bb)))


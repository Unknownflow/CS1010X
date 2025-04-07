#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 3 of 3
# ============
# Write your function here. It should return a rune.

def runeception(function, size):
    result = function
    
    for i in range(2, size):
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
                overlay_frac(
                    (0.25*i)/(i+1),
                    blank_bb,
                    result,
                    
                    ),
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

rune = runeception(make_cross(rcross_bb), 10)

#show(rune)
# Use one of the following methods to display your rune:
# stereogram(rune)
anaglyph(rune)
#hollusion(rune)

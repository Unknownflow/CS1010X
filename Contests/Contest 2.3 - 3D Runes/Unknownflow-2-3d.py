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

# Entry 2 of 3
# ============
# Write your function here. It should return a rune.

def clover():
    return beside(
        stack(
            eighth_turn_left(heart_bb), # top left
            eighth_turn_left(quarter_turn_left(heart_bb)) # bottom left
            ),
        stack(
            eighth_turn_left(flip_horiz(quarter_turn_left(heart_bb))), # top right
            eighth_turn_left(flip_vert(heart_bb)) # bottom right
            )
        )


def cloverception(function, size):
    result = function
    clover_img = image_to_painter("clover.png")
    
    for i in range(2, size):
        n = (i-1) * (i-1)

        if i % 2 == 0: # add space between the inner clover and outer clover
            n = i * i
            function = clover_img
        else:
            function = clover()
        
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
                    (0.25 * i) / (i + 1),
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

rune = cloverception(clover(), 5)


# Use one of the following methods to display your rune:
stereogram(rune)
#anaglyph(rune)
#hollusion(rune)

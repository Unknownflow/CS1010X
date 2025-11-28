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

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.

def moving_diamonds(function, size):
    result = function

    for i in range(2, size, 2):
        # place i pic at the side of the rune
        result = quarter_turn_left(
                    stack_frac(
                        i/(i+1),
                        result,
                        overlay_frac( # make the side with smaller diamond a lighter shade of grey
                            (0.75 * i)/(i + 1),
                            blank_bb,
                            quarter_turn_left(
                                stackn(i, function)
                                )
                            )
                        )
                    )

        # place i+1 pic at the bottom of the rune
        result = stack_frac(
                    i/(i+1),
                    result,
                    overlay_frac( # make the side with smaller diamond a lighter shade of grey
                        (0.75 * i)/(i + 1),
                        blank_bb,
                        quarter_turn_left(
                            stackn(i+1, function)
                            )
                        )
                    )

        result = quarter_turn_right(result) # need to turn 1/4 to the right to its orig position since it was turn 1/4 to the left initially

    # replicate the rune 4 times with the biggest pic at the corner
    result = beside(
                stack(
                    quarter_turn_left(result), # top left
                    quarter_turn_left(quarter_turn_left(result)) # bottom left
                    ),
                stack(
                    result, # top right
                    quarter_turn_right(result) # bottom right
                    )
                )
    return result


rune = moving_diamonds(make_cross(corner_bb), 15)
#show(rune)
# Use one of the following methods to display your rune:
#stereogram(rune)
#anaglyph(rune)
hollusion(rune)

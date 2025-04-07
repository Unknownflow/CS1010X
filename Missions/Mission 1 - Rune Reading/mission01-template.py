#
# CS1010X --- Programming Methodology
#
# Mission 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


##########
# Task 1 #
##########

'''
def mosaic(*params):
    # Fill in code here
    rune_1, rune_2, rune_3, rune_4 = params
    return beside(
            stack(rune_4, rune_3),
            stack(rune_1, rune_2)
        )
'''

def mosaic(rune_1, rune_2, rune_3, rune_4):
    # Fill in code here
    return stack(
            beside(rune_4, rune_1),
            beside(rune_3, rune_2)
        )

# Test
#show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))
show ( mosaic ( heart_bb , pentagram_bb , circle_bb , ribbon_bb ))

##########
# Task 2 #
##########

def simple_fractal(params):
    # Fill in code here
    rune = params
    return beside(
            rune,
            stack(rune, rune)
        )

# Test
#show(simple_fractal(make_cross(rcross_bb)))
#show ( simple_fractal ( heart_bb ))


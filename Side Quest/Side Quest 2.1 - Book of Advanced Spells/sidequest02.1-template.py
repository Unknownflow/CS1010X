#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi

##########
# Task 1 #
##########

def tree(n, rune):
    # Fill in code here
    final_rune = blank_bb

    for i in range(n):
        final_rune = overlay_frac(1/(i+1), scale((n-i)/n, rune), final_rune)
        
    return final_rune

# Test
#show(tree(4, circle_bb))


##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

def helix(rune, n):
    # Fill in code here
    deg_to_rad_constant = pi / 180
    angle = 360 / n * deg_to_rad_constant
    curr_angle = 360 / n * deg_to_rad_constant
    radius = 1/2 - 1/n
    final_rune = blank_bb
    
    for i in range(2, n+2):
        # calculate the vertical and horizontal dist for each rune
        x = radius * cos(curr_angle)
        y = radius * sin(curr_angle)

        # overlay the runes as more runes are added
        final_rune = overlay_frac(
            1/(i-1),
            translate(x, y, scale(2/n, quarter_turn_left(rune))), # position of new rune
            final_rune
            )

        # increment the angle
        curr_angle = angle * i

    return quarter_turn_right(final_rune)

# Test
show(helix(make_cross(rcross_bb), 9))
#show(helix(make_cross(rcross_bb),12))
#show(helix(nova_bb,9))

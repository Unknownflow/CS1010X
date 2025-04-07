#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(rune, n):
    # Fill in code here
    # base case where n is 1
    if n == 1:
        return rune
    else:
        return beside(rune, stackn(2, fractal(rune, n-1)))


# Test
show(fractal(make_cross(rcross_bb), 4))
#show(fractal(make_cross(rcross_bb), 3))
#show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(rune, n):
    # Fill in code here
    final_rune = rune

    for i in range(1, n):
        final_rune = beside(rune, stackn(2, final_rune))

    return final_rune

# Test
#show(fractal_iter(make_cross(rcross_bb), 3))
#show(fractal_iter(make_cross(rcross_bb), 3))
#show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(rune1, rune2, n):
    # Fill in code here
    if n == 1:
        return rune1
    else:
        return beside(rune1, stackn(2, dual_fractal(rune2, rune1, n-1)))


# Test
#show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 5))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(rune1, rune2, n):
    # Fill in code here
    # determine what is the rune in the rightmost position
    if n % 2 == 0:
        final_rune = rune2
        prev = 2
    else:
        final_rune = rune1
        prev = 1

    for i in range(1, n):
        # check what rune was used previously used and update previous rune used for the fractal
        if prev == 2:
            final_rune = beside(rune1, stackn(2, final_rune))
            prev = 1
        else:
            final_rune = beside(rune2, stackn(2, final_rune))
            prev = 2

    return final_rune

# Test
#show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 5))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########

def steps(rune1, rune2, rune3, rune4):
    # Fill in code here
    top_right = overlay(blank_bb, overlay(blank_bb, rune1)) # lowest level 
    bottom_right = overlay(blank_bb, rune2) # 3rd highest level
    bottom_left = overlay(overlay(blank_bb, rune3), blank_bb) # 2nd highest level
    top_left = rune4 # highest level
    return stack(
            beside(top_left, top_right),
            beside(bottom_left, bottom_right)
        )

# Test
#show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))

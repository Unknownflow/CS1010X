#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

draw_connected_scaled(200,connect_ends ( unit_line , unit_circle ))
draw_connected_scaled(200, connect_ends ( revert ( unit_line ), unit_circle ))


def dragonize(order, curve):
    if order == 0:
        return curve
    else:
        c = dragonize(order-1, curve)
        return put_in_standard_position(connect_ends(rotate(-pi/2)(revert(c)), c))

# test:
draw_connected_scaled(4096, dragonize(12, unit_line))

#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def kochize(level):
    if level == 0:
        return unit_line
    else:
        return put_in_standard_position(
            connect_ends(
                kochize(level-1), 
                connect_ends(
                    rotate(pi/3)(kochize(level-1)), 
                    connect_ends(
                        rotate(-pi/3)(kochize(level-1)),
                        kochize(level-1)
                    )
                )
            ))

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))

# testing
# show_connected_koch(0, 4000)
# show_connected_koch(1, 4000)
# show_connected_koch(2, 4000)
# show_connected_koch(5, 4000)
# show_connected_koch(4, 4000)

##########
# Task 2 #
##########

def snowflake():
    koch_curve = kochize(5)
    return put_in_standard_position(
        connect_ends(
            rotate(2/3*pi)(koch_curve),
            connect_ends(
                koch_curve,
                rotate(-2/3*pi)(koch_curve)
            )
        ))

draw_connected_scaled(10000, snowflake())

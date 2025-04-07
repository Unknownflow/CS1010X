#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

# draw_connected_scaled(200, unit_circle)
# draw_connected_scaled(200, alternative_unit_circle)

# draw_points_scaled(200, unit_circle)
# draw_points_scaled(200, alternative_unit_circle)

# When I used draw_points to draw out the circles, the points for the alternative_unit_circle appear closer to each other when t is closer to 0 and the distance increases as t approaches 1 as compared to the unit_circle where the distance between the points is the same from t=0 to t=1. 

# This difference exists as the unit_circle uses sin(2*pi*t) for its x value and cos(2*pi*t) for its y value whereas the alternative_unit_circle uses sin(2*pi*t*t) for its x value and cos(2*pi*t*t) for its y value.

# For a sin(2*pi*t) graph and a cos(2*pi*t) graph, the gradient of the graph is relatively constant except its turning points where gradient is 0 and this suggests that the difference in the distance will remain constant. For a sin(2*pi*t*t) and a cos(2*pi*t) graph, the gradient at the start is relatively constant but it gradually increases and this would suggest that the difference in the distance will also increase as t increases.

##########
# Task 2 #
##########

# (a)
def spiral(t):
    return make_point(t*sin(2*pi*t), t*cos(2*pi*t))

def heart(t):
    if t < 0.5:
        return spiral(2*t)
    else:
        return scale_xy(-1, 1)(spiral)(2*t-1)

draw_connected_scaled(1000, heart)

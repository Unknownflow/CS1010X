#
# CS1010X --- Programming Methodology
#
# Mission 5
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

def connect_ends(curve1, curve2):
    curve1_end = curve1(1)
    curve2_start = curve2(0)
    
    # get x and y coord of curve 1 end pt
    x1 = x_of(curve1_end)
    y1 = y_of(curve1_end)

    # get x and y coord of curve 2 start pt
    x2 = x_of(curve2_start)
    y2 = y_of(curve2_start)

    # find out how much to translate curve 2 start pt to curve 1 end pt position
    translation_x = x1 - x2
    translation_y = y1 - y2

    return connect_rigidly(curve1, translate(translation_x, translation_y)(curve2))


# draw_connected_scaled(200, connect_ends(arc, unit_line))
# draw_connected_scaled(200, connect_ends(translate(5,5)(arc), translate(1,1)(unit_line)))

##########
# Task 2 #
##########
def show_connected_gosper ( level ):
    squeezed_curve = squeeze_curve_to_rect (-0.5 , -0.5 , 1.5 , 1.5) \
    ( gosper_curve ( level ))
    draw_connected ( 200 , squeezed_curve )


def gosper_curve(level, curve):
    return repeated(gosperize, level)(curve)

def show_points_gosper(level, num_points, initial_curve):
    squeezed_curve = squeeze_curve_to_rect(-0.5, -0.5, 1.5, 1.5) \
    (gosper_curve(level, initial_curve))
    draw_points(num_points, squeezed_curve)

# show_points_gosper ( 2 , 200 , unit_line )
# show_connected_gosper(2)
# show_points_gosper(5, 500, arc)
# show_points_gosper(7, 1000, arc)

##########
# Task 3 #
##########

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn), rotate(-theta)(curve_fn)))
    return inner_gosperize

# testing
draw_connected(200, your_gosper_curve_with_angle(10, lambda lvl: pi/(2+lvl)))
draw_connected(200, your_gosper_curve_with_angle(5, lambda lvl: (pi/(2+lvl))/(pow(1.3, lvl))))
draw_connected(200, your_gosper_curve_with_angle(3, lambda lvl: pi/(2+lvl)))
draw_connected_scaled(200, your_gosper_curve_with_angle(10,lambda lvl: pi/(2+lvl)))
#
# CS1010S --- Programming Methodology
#
# Sidequest 8.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from planets import *

# Set up the environment of the simulation
planets = (Earth, Mars, Moon)

plot_planets(planets, Mars)

##########
# Task 1 #
##########
# a)
# Follows trigonometry angle.
# E.g. 0 degree -> East
# E.g. 90 degree -> North

from math import sin, cos, radians
def get_velocity_component(angle, velocity):
    angle_rad = radians(angle)
    return (velocity * cos(angle_rad), velocity * sin(angle_rad))

# print(get_velocity_component(30, 50)) #(43.30127018922194, 24.999999999999996)
# note that the exact values of each component may differ slightly due to differences in precision

# b)
from math import sqrt
def calculate_total_acceleration(planets, current_x, current_y):
    result = [0, 0]
    
    for planet in planets:
        x_coord = get_x_coordinate(planet)
        y_coord = get_y_coordinate(planet)
        mass = get_mass(planet)

        # calculate r, r_x and r_y using the formulas
        r_x = x_coord - current_x
        r_y = y_coord - current_y
        r = sqrt((x_coord - current_x) ** 2 + (y_coord - current_y) ** 2)

        # calculate acceleration for x and y component
        acc_x = (G * mass * r_x) / (r ** 3)
        acc_y = (G * mass * r_y) / (r ** 3)

        result[0] = result[0] + acc_x
        result[1] = result[1] + acc_y

    return result


# print(calculate_total_acceleration(planets, 0.1, 0.1)) #(-1511.54410020574, -1409.327982470404)

# c)
# Do not change the return statement
def f(t, Y):
    rx, ry, vx, vy = Y
    ax, ay = calculate_total_acceleration(planets, rx, ry)
    return np.array([vx, vy, ax, ay])

np.set_printoptions(precision=3)
print(f(0.5, [0.1, 0.1, 15.123, 20.211])) #[ 15.123 20.211 -1511.544 -1409.328]

##########
# Task 2 #
##########

# Uncomment and change the input parameters to alter the path of the spacecraft
# vx, vy = get_velocity_component(78, 28.5)
vx, vy = get_velocity_component(75.5, 27.3)
# vx, vy = get_velocity_component(74, 27.5)

# vx, vy = get_velocity_component(77, 27.3)

##############################################################################################
# Uncomment the following line to start the plot
start_spacecraft_animation(vx, vy, f)

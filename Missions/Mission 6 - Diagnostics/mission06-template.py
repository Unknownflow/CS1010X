#
# CS1010X --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# from diagnostic import *
# from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:

# def your_gosper_curve_with_angle(level, angle_at_level):
#     if level == 0:
#         return unit_line
#     else:
#         return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

# def your_gosperize_with_angle(theta):
#     def inner_gosperize(curve_fn):
#         return put_in_standard_position(connect_ends(rotate(theta)(curve_fn), rotate(-theta)(curve_fn)))
#     return inner_gosperize





# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(1000)(0.1), 500)

# Choose a significant level for testing for all three sets of functions.
# profile_fn(lambda: gosper_curve(50)(0.1), 50)

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

# num_executions = 5
# gosper_curve_times = []

# for i in range(num_executions):
#     gosper_curve_times.append(profile_fn(lambda: gosper_curve(50)(0.1), 100))

# print('gosper_curve avg time:', sum(gosper_curve_times)/num_executions)
# print('gosper_curve timings:', gosper_curve_times)

# Time measurements
# 10.86320000467822
# 11.436200002208352
# 12.456100026611239
# 11.185699957422912
# 11.391300009563565

# Average: 11.466500000096858


# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# gosper_curve_with_angle_times = []

# for i in range(num_executions):
#     gosper_curve_with_angle_times.append(profile_fn(lambda: gosper_curve_with_angle(50, lambda lvl : pi/4)(0.1), 100))

# print('gosper_curve_with_angle avg time:', sum(gosper_curve_with_angle_times)/num_executions)
# print('gosper_curve_with_angle timings:', gosper_curve_with_angle_times)

# Time measurements
# 11.937599978409708
# 12.03049998730421
# 11.858200014103204
# 10.904799972195178
# 12.375999998766929

# Average: 11.821419990155846

#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# your_gosper_curve_with_angle_times = []

# for i in range(num_executions):
#     your_gosper_curve_with_angle_times.append(profile_fn(lambda: your_gosper_curve_with_angle(50, lambda lvl : pi/4)(0.1), 100))

# print('your_gosper_curve_with_angle avg time:', sum(your_gosper_curve_with_angle_times)/num_executions)
# print('your_gosper_curve_with_angle timings:', your_gosper_curve_with_angle_times)

# Time measurements
# 1105.2491999580525
# 1092.5123000051826
# 1091.6759999818169
# 1091.193199972622
# 1098.8101999973878

# Average: 1095.8881799830124


# Conclusion:
# The average time taken for each function to complete in ascending order is gosper_curve (11.47s), 
# gosper_curve_with_angle (11.82s) and your_gosper_curve_with_angle (1095.89s). The times are rounded
# to 2dp.

# gosper_curve_with_angle and your_gosper_curve_with_angle is more customizable as you can customize
# the angle_at_level while gosper_curve cannot do so and hence it is more customized.
# gosper_curve which is more customized have a small advantage (in speed) as compared to the more
# customizable gosper_curve_with_angle and gosper_curve also has a more significant advantage (in speed) 
# as compared to the more customizable your_gosper_curve_with_angle.


##########
# Task 2 #
##########

#  1) Yes joe_rotate works and achieves the same purpose as the output remains the same.


#  2) For the rotate function, pt stores the value of curve(t) and curve(t) will only need to be called
#     once each time rotate is executed as compared to the joe_rotate function where curve(t) needs to be
#     executed twice (x, y = x_of(curve(t)), y_of(curve(t))) each time rotate is executed. 
#     The gosper_curve function executes repeated on gosperize and gosperize contains the rotate function. 
#     Hence, rotate and joe_rotate in gosperize will be called recursively until the base case is reached. 

#     For joe_rotate, curve(t) will be executed twice at each recursive step until its base case and this 
#     will result in a process where time is exponential in the level as compared to rotate where curve(t) 
#     is only executed once at each recursive step, hence resulting in a process where time is linear in 
#     the level.

##########
# Task 3 #
##########

    
#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1          3              4
#                      2          5              10
#                      3          7              22
#                      4          9              46
#                      5          11             94
#
#  Evidence of exponential growth in joe_rotate.

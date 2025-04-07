from diagnostic import *
from hi_graph_connect_ends import *

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

trace(fib)
fib(3)
untrace(fib)
fib(3)


# original_rotate = rotate
# replace_fn(rotate, joe_rotate)
# for i in range(1, 6):
#     print(i)
#     trace(x_of)
#     x_of(gosper_curve(i)(0.5))
#     untrace(x_of)

# 1
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B1A0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B560>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B1A0>)
# --> 0.0
# 2
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B240>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B560>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B240>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B560>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B240>)
# --> 0.0
# 3
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B740>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B600>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B740>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B600>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B740>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B600>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95B740>)
# --> 0.0
# 4
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BA60>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BB00>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BA60>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BB00>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BA60>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BB00>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BA60>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BB00>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BA60>)
# --> 0.0
# 5
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BE20>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BE20>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BE20>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BE20>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BE20>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x000002223D95BBA0>)
# --> 0.0


# joe_trace

# 1
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B2E0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B6A0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B6A0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B2E0>)
# --> 0.0
# 2
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B380>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B6A0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B6A0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B380>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B6A0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B6A0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B380>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B380>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B6A0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B380>)
# --> 0.0
# 3
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B740>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B740>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B740>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B740>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B740>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B740>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B740>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B740>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B740>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B740>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B740>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# 4
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BC40>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BBA0>)
# --> 0.0
# 5
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0BCE0>)
# --> 0.0
# x_of(<function make_point.<locals>.<lambda> at 0x0000029708A0B880>)
# --> 0.0
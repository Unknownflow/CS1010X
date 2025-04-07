from math import *

def exception_function(f, rejected_input, new_output):
    def helper(num):
        if num == rejected_input:
            return new_output
        else:
            return f(num)
        
    return helper

#################
# DO NOT REMOVE #
#################
new_sqrt = exception_function(sqrt, 7, 2)
print(new_sqrt(9))
print(new_sqrt(16))
print(new_sqrt(7))
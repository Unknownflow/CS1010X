from math import *

def exception_function(f, rejected_input, new_output):
    def helper(num):
        if num == rejected_input:
            return new_output
        else:
            return f(num)
        
    return helper

def usually_double(x):
    return x + x

def new_double(x):
    return min(
        exception_function(usually_double, 4, 0)(x), 
        exception_function(usually_double, 7, 0)(x), 
        exception_function(usually_double, 11, 0)(x)
        )

print(usually_double(7))
print(usually_double(4))
print(new_double(4))
print(new_double(7))
print(new_double(11))
print(new_double(10))
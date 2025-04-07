# Three Integers

# Implement a function get_hundredth(a, b, c) that takes in 3 positive integers as arguments and returns a tuple of digits at the respective hundredth position.

# If a given integer is less than 100, its hundredth position can be viewed as 0. If the input is invalid, return None for that integer. 

def get_hundredth(a,b,c):

    res = ()

    for num in (a, b, c):

        if type(num) != int or num <= 0:

            res += (None,)

        elif num < 100:

            res += (0,)

        else:

            res += (int(str(num)[-3]),)

    return res
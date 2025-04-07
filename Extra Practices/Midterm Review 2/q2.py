from math import *

def largest_square_pyramidal_num(n) :
    pyramidal_num = 1
    curr_square = 2

    while pyramidal_num < n:
        square = curr_square * curr_square
        if square + pyramidal_num > n:
            return pyramidal_num
        else:
            pyramidal_num += square
            curr_square += 1
    
    return pyramidal_num
   
def test_square_pyramidal(n) :
    # You can use this function to 
    # test largest_square_pyramidal_num()
    return largest_square_pyramidal_num(n)

print(test_square_pyramidal(1))
print(test_square_pyramidal(9))
print(test_square_pyramidal(14))

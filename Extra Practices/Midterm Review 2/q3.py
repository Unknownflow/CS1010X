from math import *

# def largest_square_pyramidal_num_rec(n):
#     res = 0
#     curr_square = 1

#     def helper(n, curr_square, res):
#         square = curr_square * curr_square
#         if n - square < 0:
#             return res
#         else:
#             return helper(n-res, curr_square+1, res+square)
    
#     return helper(n, curr_square, res)
    
# print(largest_square_pyramidal_num_rec(1))
# print(largest_square_pyramidal_num_rec(9))
# print(largest_square_pyramidal_num_rec(14))

from math import *

def largest_square_pyramidal_num_rec(n) :
    def is_square_pyramidal_num(n):
        pyramidal_num = 1
        curr_square = 2

        while pyramidal_num < n:
            square = curr_square * curr_square
            if square + pyramidal_num > n:
                return False
            else:
                pyramidal_num += square
                curr_square += 1
        return True
    
    if is_square_pyramidal_num(n):
        return n
    else:
        return largest_square_pyramidal_num_rec(n-1)
    

print(largest_square_pyramidal_num_rec(1))
print(largest_square_pyramidal_num_rec(9))
print(largest_square_pyramidal_num_rec(14))
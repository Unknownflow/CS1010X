# Pascal Triangle

# Implement a function pascal(n) that takes a positive integer number n and returns a Pascal's triangle with that number of rows represented by a tuple. You should use recursion to solve this problem.

def pascal(n):

    if n == 1:

        return ((1,),)

    elif n == 2:

        return pascal(1) + ((1,1),)

    else:

        new_row = (1,)

        prev_row = (pascal(n-1)[-1])

        for i in range(len(prev_row)-1):

            new_row += (prev_row[i] + prev_row[i+1],)

        new_row += (1,)

        

        return pascal(n-1) + (new_row, )
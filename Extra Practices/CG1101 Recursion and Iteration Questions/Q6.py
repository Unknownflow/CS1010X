#Question 6

#Recursive Sum

#Write a recursive function recursive_sum to accept a non-negative integer x and calculate f(x) based on the following formula.


def recursive_sum(n):

    # Fill in your code here

    # base case where n = 0, 1 or 2

    if 0 <= n <= 2:

        return 1

    

    # when n is even, return f(n-1) + f(n-2) + f(n-3) 

    # else return f(n-1) + f(n-2)

    if n % 2 == 0:

        return recursive_sum(n-1) + recursive_sum(n-2) + recursive_sum(n-3)

    else:

        return recursive_sum(n-1) + recursive_sum(n-2)

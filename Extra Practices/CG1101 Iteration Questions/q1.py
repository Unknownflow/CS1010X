# Question 1

# Perfect Number

# A perfect number is a positive integer that is equal to the sum of its proper divisors. A proper divisor is a positive integer other than the number itself that divides the number evenly (i.e. no remainder). For example, 6 is the smallest perfect number, because the sum of its proper divisors 1, 2, and 3 is equal to 6. 8 is not a perfect number because 1 + 2 + 4 is not equal to 8.

# Write a function perfect_number that accepts a positive integer in the range [1, 10000] and returns True/False depending on whether the number is a perfect number or not.

from math import sqrt

def perfect_number(number):

    # Your code here

    # base case where number is 1

    if number == 1:

        return False

    

    sum_divisor = 1

    for i in range(2, round(sqrt(number))+1):

        if number % i == 0:

            # add to sum_divisor if i can be divisible by number

            sum_divisor += i

            sum_divisor += number / i 

    if sum_divisor == number:

        return True

    else:

        return False

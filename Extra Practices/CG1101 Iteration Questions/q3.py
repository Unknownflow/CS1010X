#Question 3
#Invert Number

#Write a function invert_number that reads in a positive integer, reverses the order of each of its digit and returns out the inverted value. For example, if input number is 12345, your program output should be 54321.

def invert_number(num):

    # Fill in your code here

    result = 0

    

    while num != 0:

        result *= 10

        remainder = num % 10

        result += remainder

        num //= 10

        

    return result

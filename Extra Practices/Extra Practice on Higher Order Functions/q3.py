#Question 3

#*Hard* Basic Morphology - Part 1

#We have previously learnt about numbers and how they can be easily converted from one base to another.

#Recall that binary numbers are represented with only two symbols, and as such, the non-negative integers form the following sequence.

#0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111, 10000, 10001

#Their decimal counterparts would be 0 to 17. Write a function decimal_to_binary, that takes a non-negative decimal integer, and converts it into its binary representation, a string.

def decimal_to_binary(number):

    # code to convert number into its binary representation

    bin_num = ""

    if number == 0:

        return "0"

    

    while number != 0:

        remainder = number % 2

        bin_num = str(remainder) + bin_num

        number //= 2

      

    return bin_num

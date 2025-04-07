#Question 6

#*Hard* Basic Morphology - Part 3

#Now, converting from decimal to other bases is useful, but we need to be able to convert back too!

#Write a function hexadecimal_to_decimal that takes a string representation of a hexadecimal number and converts it into a decimal number.


def hexadecimal_to_decimal(hex_number):

    # return the decimal number that hex_number represents

    hex_arr = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    result = 0

    length = len(hex_number)

    

    for i in range(length):

        hex_char = hex_number[i]

        if hex_char in "ABCDEF":

            hex_val = hex_arr[hex_char]

        else:

            hex_val = int(hex_char)

        

        result += hex_val * (16 ** (length-i-1))

    return result

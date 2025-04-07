#Question 7

#*Hard* Basic Morphology - Part 4

#To step things up, now, we want to be able to convert a number from any base to decimal.

#Write a function make_n_ary_to_decimal_converter that takes a number n where 1 < n < 17 and returns a number converter that converts string representations of numbers of base n into decimal numbers.

def make_n_ary_to_decimal_converter(n):

    # return a number converter that takes a string representation of a base n number and returns its decimal equivalent

    def converter(number):

        hex_arr = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

        result = 0

        length = len(number)

        

        for i in range(length):

            hex_char = number[i]

            if hex_char in "ABCDEF":

                hex_val = hex_arr[hex_char]

            else:

                hex_val = int(hex_char)

            

            result += hex_val * (n ** (length-i-1))

        

        return result

    return converter

binary_to_decimal = make_n_ary_to_decimal_converter(2)

octal_to_decimal = make_n_ary_to_decimal_converter(8)

hexadecimal_to_decimal = make_n_ary_to_decimal_converter(16)

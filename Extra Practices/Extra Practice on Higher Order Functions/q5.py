#Question 5

#*Hard* Basic Morphology - Part 2

#Other than just binary and decimal, we can have numbers of any base. Common bases that we work with include octal, hexadecimal and base64.

#Here is a table of numbers from 0 to 15 in each of the above mentioned bases except base64.

#https://web.archive.org/web/20190714220120/http://www.themathwebsite.com/TogglerNumbers/Octal.GIF

#Write a function make_decimal_to_n_ary_converter that accepts a number n where 1 < n < 17, and returns a number converter that converts a given decimal number into that of base n.



def make_decimal_to_n_ary_converter(n):

    # return a number converter that takes a decimal number and returns its string representation in base n

    hex_char = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    def converter(number):

        result = ""

        

        if number == 0:

            return "0"

        

        while number > 0:

            remainder = number % n

            number //= n

            if remainder >= 10:

                result = hex_char[remainder] + result

            else:

                result = str(remainder) + result

        

        return result

    

    return converter

decimal_to_binary = make_decimal_to_n_ary_converter(2)

decimal_to_octal = make_decimal_to_n_ary_converter(8)

decimal_to_hexadecimal = make_decimal_to_n_ary_converter(16)

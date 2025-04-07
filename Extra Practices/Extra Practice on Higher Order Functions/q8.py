#Question 8

#*Hard* Basic Morphology - Part 5

#Finally, we want to be able to convert numbers from any base, to any other base!

#Write a function make_p_ary_to_q_ary_converter that takes two numbers p and q, and returns a converter that takes a string representation of a number in base p, and returns the string representation of the number in base q.
#Note that make_decimal_to_n_ary_converter and make_n_ary_to_decimal_converter have already been defined for you.

#As usual, assume 1 < p, q < 17.

def compose(f, g):

    return lambda x: f(g(x))

def make_p_ary_to_q_ary_converter(p, q):

    # return a number converter that takes a string representation of a number in base p and returns the string representation of that number in base q

    hex_to_num = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    num_to_hex = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    def make_decimal_to_n_ary_converter(n, number):

        # return a number converter that takes a decimal number and returns its string representation in base n

        result = ""

        

        if number == 0:

            return "0"

        

        while number > 0:

            remainder = number % n

            number //= n

            if remainder >= 10:

                result = num_to_hex[remainder] + result

            else:

                result = str(remainder) + result

        

        return result

    def make_n_ary_to_decimal_converter(n, number):

      # return a number converter that takes a string representation of a base n number and returns its decimal equivalent

        result = 0

        length = len(number)

        

        for i in range(length):

            hex_char = number[i]

            if hex_char in "ABCDEF":

                hex_val = hex_to_num[hex_char]

            else:

                hex_val = int(hex_char)

            

            result += hex_val * (n ** (length-i-1))

        

        return result

    

    def converter(number):

        # p and q are same base, means no conversion needed

        if p == q:

            return number

            

        dec = make_n_ary_to_decimal_converter(p, number)

        return make_decimal_to_n_ary_converter(q, dec)

        

    return converter

binary_to_octal = make_p_ary_to_q_ary_converter(2, 8)

hexadecimal_to_binary = make_p_ary_to_q_ary_converter(16, 2)

octal_to_hexadecimal = make_p_ary_to_q_ary_converter(8, 16)

octal_to_binary = make_p_ary_to_q_ary_converter(8, 2)

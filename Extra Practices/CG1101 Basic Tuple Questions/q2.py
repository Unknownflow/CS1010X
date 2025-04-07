# Standard Deviation

# Implement a function def deviation(real_numbers) that computes the standard deviation of n real numbers. It takes in a tuple of n real numbers as an input.

# The standard deviation s is computed according to the following formula:


# The variable x̄ is the average of n input values x1 through xn.

# You may assume that 0 < n < 10. Check the test cases for input and output format. Your output should be in two-decimal places.

def deviation(real_numbers):

    # code to calculate the standard deviation based on n real numbers

    sum_num = 0

    num_count = 0

    for num in real_numbers:

        sum_num += num

        num_count += 1

    mean = sum_num / num_count

    res = 0

    for num in real_numbers:

        res += (num - mean) ** 2

    res = round((res / num_count) ** 0.5, 2)

    return res
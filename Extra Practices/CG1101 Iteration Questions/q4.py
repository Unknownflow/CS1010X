#Question 4
#Reversed Numbers

#You are to write a single function reversed_numbers that reads two positive integers low and high, that returns how many integers in the range [low, high] whose reverse is the same as the original value. You may assume that low ≤ high. For example, if low is 150 and high is 202, then there are 6 integers in the range [150, 202] whose reverse is the same as itself. They are: 151, 161, 171, 181, 191, and 202.

#You are given the invert_number function from the previous task. You are not allowed to use any array / string methods for this task.

def reversed_numbers(low, high):

    # Fill in your code here

    count = 0

    

    for i in range(low, high+1):

        if invert_number(i) == i:

            count += 1

    return count

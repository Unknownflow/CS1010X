#Question 2

#Print Pattern

#Write a function pattern that reads in a positive integer input and returns a stylized pattern as demonstrated in the sample runs.

def pattern(number):

    # Fill in your code here

    result = ""

    

    for i in range(1, number+1):

        result += "#"

        result += "-" * i

        

    return result

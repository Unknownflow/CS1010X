#Question 5
#Count Substring

#Write a program count_substring that reads a string (less than 20 characters) from the user and stores it into a character array.

#Using just one loop, devise an algorithm that counts the number of substrings that begin with character 'A' and ends with character 'X'. For example, given the input string "CAXAAYXZA", there are four substrings that begin with 'A' and ends with 'X', namely: "AX", "AXAAYX", "AAYX", and "AYX".

#You can assume that the input string is composed of English upper case letters only.

def count_substring(string):

    # Fill in your code here

    count = 0

    count_A = 0

    

    for char in string:

        if char == "A":

            count_A += 1

        elif char == "X":

            count += count_A

            

    return count

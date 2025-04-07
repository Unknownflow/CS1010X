#Question 1

#Legendre's Conjecture

#Legendre's conjecture (proposed by Adrien-Marie Legendre in 1912) states that there is at least one prime number in range [n^2, (n + 1)^2] for every positive integer n.

#Implement the function legendre that takes in an input parameter n and tests Legendre's conjecture over a range of numbers from 1 up to the input number n.

#This means if the input is 4, you should check that there is at least one prime between 1^2 and 2^2, and at least one prime between 2^2 and 3^2, and at least one prime between 3^2 and 4^2, and at least one prime between 4^2 and 5^2.

#As you might have guessed, the one and only return value of this function is True. You can pass this question by simply writing return True but you will just be compromising your own learning.

#Note: Coursemology will limit your runtime. You will need an efficient way of doing this to clear the question

from math import sqrt

def legendre(n):

    # code to test Legendre's conjecture over a range of numbers from 1 up to the input number n.

    def isPrime(n):

        # check whether the number is divisible by i up till sqrt(n)+1

        if n <= 1:

            return False

        upper_bound = int(sqrt(n))+1

        

        for i in range(2, upper_bound):

            # if number is not prime, return false

            if n % i == 0:

                return False

            

        # otherwise return true

        return True 

    

    for i in range(1, n+2):

        count = 0

        

        # loop through range of i**2 to (i+1)**2 to check for prime numbers

        for j in range(i**2, (i+1)**2 + 1):

            if isPrime(j):

                count += 1

                break

        # if there is no prime number in the range

        if count == 0:

            return False

    return True

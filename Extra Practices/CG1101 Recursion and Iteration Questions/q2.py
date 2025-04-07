#Question 2

#Legendre's Conjecture - Part 2!

#Now, implement the function legendre_n to test Legendre's Conjecture for a specific number n.

#Given an integer n, the function legendre_n should return the number of prime numbers between n^2 and (n+1)^2.

from math import sqrt, ceil

def legendre_n(n):

    # code to test Legendre's conjecture over a range of numbers from 1 up to the input number n.

    def isPrime(n):

        # check whether the number is divisible by i up till sqrt(n)+1

        if n <= 1:

            return False

        upper_bound = int(sqrt(n))+1

        for i in range(2, upper_bound):

            if n % i == 0:

                return False # if number is not prime, return false

        return True 

    count = 0

    lower_bound = n ** 2

    upper_bound = (n+1) ** 2 + 1

    

    for i in range(lower_bound, upper_bound):

        if isPrime(i):

            count += 1

    return count

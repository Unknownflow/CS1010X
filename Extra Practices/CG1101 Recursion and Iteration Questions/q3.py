#Question 2

#Goldbach's Conjecture

#Goldbach's conjecture (proposed by Christian Goldbach in 1742) is one of the oldest unsolved problems in number theory. It states: every even integer greater than 2 can be written as the sum of two primes.

#Implement a function:
#def goldbach(n):
#to test Goldbach's Conjecture over a range of even numbers from 4 up to the input number n. This means that if the input is 8, you should check that 4 can be written as a sum of two primes (2 + 2) and 6 can be written as a sum of two primes (3 + 3) and 8 can be written as a sum of two primes (3 + 5).

#You may assume that input number n is always greater or equal to 4.

from math import sqrt

def goldbach(n):

    # code to test Goldbach's Conjecture on an input n

    

    def isPrime(n):

        # check whether the number is divisible by i up till sqrt(n)+1

        if n <= 1:

            return False

        upper_bound = int(sqrt(n))+1

        for i in range(2, upper_bound):

            if n % i == 0:

                return False # if number is not prime, return false

        return True 

    primes_arr = []

    # create an array of primes

    for i in range(2, n):

        if isPrime(i):

            primes_arr.append(i)

    for i in primes_arr:

        for j in primes_arr:

            # check whether the sum of 2 primes matches n

            if i + j == n:

                return True

    return False

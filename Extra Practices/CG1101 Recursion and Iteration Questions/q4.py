#Question 2

#Maclaurin Series

#In mathematics, the Taylor series is a representation of a function as an infinite sum of terms calculated from the values of its derivatives at a single point. It may be regarded as the limit of the Taylor polynomials. Taylor series are named after the English mathematician Brook Taylor. If the series is centered at zero, the series is also called a Maclaurin series, named after the Scottish mathematician Colin Maclaurin.

#As an example, an approximation for e^x is:


#Implement a function:
#def maclaurin(x, n):
#that reads in two positive integers x and n, calculate e^x up to the nth term in the Maclaurin series. i.e.,   

#Define n! as a function factorial in your program. You should correct your output to 3 decimal places. (You may use round(value, n) to round value to n decimal places.)


def maclaurin(x, n):

    # code that approximates e^x up to the nth term

    def factorial(n):

        # returns n!

        result = 1

        for i in range(2, n+1):

            result *= i

        return result

    result = 1

    # adds up ith term until x^(n-1) / (n-1)!

    for i in range(1, n):

        result += (x ** i) / (factorial(i))

    return round(result, 3)

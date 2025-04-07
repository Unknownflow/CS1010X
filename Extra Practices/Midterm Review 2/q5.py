from math import *

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

def test_even_num(n):
    return n % 2 == 0

def test_prime_num(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def combine_num(op, n, test_func) :
    if n < 1:
        if op == add:
            return 0
        elif op == mul:
            return 1
    else:
        if test_func(n):
            return op(n, combine_num(op, n-1, test_func))
        else:
            return combine_num(op, n-1, test_func)

print(combine_num(add, 5, test_even_num))
print(combine_num(mul, 10, test_prime_num))
print(combine_num(mul, 5, test_even_num))
print(combine_num(add, 10, test_prime_num))
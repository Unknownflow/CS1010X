from math import *

def find_largest_num(test_func, n) :
    if n <= 0:
        return False
    elif test_func(n) :
        return n
    else :
        return find_largest_num(test_func, n-1)
    
def test_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n)+1), 2):
        if n % i == 0:
            return False
    
    return True

print(find_largest_num(test_prime, 5))
print(find_largest_num(test_prime, 9))

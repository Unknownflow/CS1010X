from math import sqrt

def foo3(n):
    if n % 2 == 0:
        return True
    for i in range(3, int(sqrt(n)+1), 2):
        if n % i == 0:
            return True
        
    return False

#Time complexity: O(n^(0.5))

print(foo3(1009))
print(foo3(100000007))
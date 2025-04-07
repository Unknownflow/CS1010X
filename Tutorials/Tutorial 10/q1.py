def collatz_distance(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return 1 + collatz_distance(n/2)
    else:
        return 1 + collatz_distance(3 * n + 1)
    

print(collatz_distance(1))
print(collatz_distance(4))
print(collatz_distance(27))
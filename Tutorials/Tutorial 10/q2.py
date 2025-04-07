def collatz_distance(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return 1 + collatz_distance(n/2)
    else:
        return 1 + collatz_distance(3 * n + 1)
    
def max_collatz_distance(n):
    max_dist = 0

    for i in range(2, n+1):
        dist = collatz_distance(i)
        if dist > max_dist:
            max_dist = dist
    
    return max_dist

print(max_collatz_distance(6))
print(max_collatz_distance(8))
print(max_collatz_distance(18))
memoize_table = {}

def memoize(f, name):
    if name not in memoize_table:
        memoize_table[name] = {}
    table = memoize_table[name]
    def helper(*args):
        if args in table:
            return table[args]
        else:
            result = f(*args)
            table[args] = result
            return result
    return helper

def collatz_distance_memo(n):
    def helper(n):
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + collatz_distance_memo(n/2)
        else:
            return 1 + collatz_distance_memo(3 * n + 1)
        
    memoize_table[n] = helper(n)
    return memoize_table[n]

def max_collatz_distance_memo(n):
    max_dist = 0

    for i in range(1, n+1):
        dist = collatz_distance_memo(i)
        if dist > max_dist:
            max_dist = dist
    
    return max_dist
        


print(max_collatz_distance_memo(6))
print(max_collatz_distance_memo(8))
print(max_collatz_distance_memo(18))

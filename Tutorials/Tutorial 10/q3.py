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
            n = n / 2
        else:
            n = 3 * n + 1

        if (n, ) in memoize_table["collatz_distance"]:
            return 1 + memoize_table["collatz_distance"][(n, )]
        else:
            return 1 + helper(n)
    
    for i in range(1, n+1):
        memoize(helper, "collatz_distance")(i)


def max_collatz_distance_memo(n):
    collatz_distance_memo(n)
    def helper(n):
        if n == 1:
            return 0
        prev = memoize_table["max_collatz_distance"][(n-1,)]
        curr = memoize_table["collatz_distance"][(n,)]

        if curr > prev:
            return curr
        else:
            return prev
    
    for i in range(1, n+1):
        memoize(helper, "max_collatz_distance")(i)

    return memoize_table["max_collatz_distance"][(n,)]


print(max_collatz_distance_memo(6))
print(max_collatz_distance_memo(8))
print(max_collatz_distance_memo(18))

print(memoize_table)
#?????
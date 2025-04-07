def make_fibonacci(n):
    if n == 0:
        return (0, )
    elif n == 1:
        return (0, 1)
    else:
        prev = make_fibonacci(n-1)
        prev_num_one = prev[-2]
        prev_num_two = prev[-1]
        res = prev_num_one + prev_num_two
        return make_fibonacci(n-1) + (res,)

print(make_fibonacci(1))
print(make_fibonacci(5))
print(make_fibonacci(10))

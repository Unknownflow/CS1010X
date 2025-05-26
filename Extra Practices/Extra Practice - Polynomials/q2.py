def fold(op, f, n):
    if n==0:
        return f(0)
    else:
        return op(f(n), fold(op, f, n-1))

def poly(coefficients, x):
    if coefficients == ():
        return 0
    return fold(lambda m, n: m + n, \
                lambda m: coefficients[m] * (x ** m), \
                len(coefficients)-1) 

print(poly((1, 2, 3, 4, 5), 3))
print(poly((1, 2, 3, 4, 5), 1))
print(poly((), 3))

def sum(term, a, next, b):
    if (a>b):
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)

def poly(coefficients, x):
    return sum(lambda y: coefficients[y] * (x ** y), 0, lambda x: x + 1, len(coefficients)-1)

print(poly((1, 2, 3, 4, 5), 3))
print(poly((1, 2, 3, 4, 5), 1))
print(poly((), 3))

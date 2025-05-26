def filtered_accumulate(op, base, term, a, next, b, filter):
    i, total = a, base
    while i <= b:
        if filter(i):
            total = op(term(i), total)
        i = next(i)
    return total

def poly_acc(coefficients, x):
    return filtered_accumulate(lambda a, b: a + b, 
                               0, 
                               lambda a: coefficients[a] * (x ** a), 
                               0, 
                               lambda a: a + 1, 
                               len(coefficients) - 1, 
                               lambda a: True)


print(poly_acc((1, 2, 3, 4, 5), 3))
print(poly_acc((1, 2, 3, 4, 5), 1))
print(poly_acc((), 3))

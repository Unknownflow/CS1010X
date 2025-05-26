def sum(term, a, next, b):
    if (a>b):
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)

def poly(coefficients, x):
    return sum(lambda y: coefficients[y] * (x ** y), 0, lambda x: x + 1, len(coefficients)-1)

def calculator_generator(coefficients):
    def helper(num):
        return poly(coefficients, num)
    return helper


p1 = calculator_generator((1, 2, 3, 4, 5))
p2 = calculator_generator(())
p3 = calculator_generator((10, 3, 5, 7, 8, 2))

print(p1(3))
print(p1(0))
print(p1(1))
print(p2(3))
print(p2(100))

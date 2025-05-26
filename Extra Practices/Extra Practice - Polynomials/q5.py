def sum(term, a, next, b):
    if (a>b):
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)
    
def filtered_accumulate(op, base, term, a, next, b, filter):
    i, total = a, base
    while i <= b:
        if filter(i):
            total = op(term(i), total)
        i = next(i)
    return total

def poly(coefficients, x):
    return sum(lambda y: coefficients[y] * (x ** y), 0, lambda x: x + 1, len(coefficients)-1)

def calculator_generator(coefficients):
    def helper(num):
        return poly(coefficients, num)
    return helper

def new_poly(coefficients, x):
    return filtered_accumulate(lambda a, b: a + b, 
                               0, 
                               lambda a: coefficients[a] * (x ** (len(coefficients)-a-1)), 
                               0, 
                               lambda a: a + 1, 
                               len(coefficients) - 1, 
                               lambda a: True)


def calculator_generator(coefficients, ptype):
    # Your code here
    def helper(num):
        if ptype == "old":
            return poly(coefficients, num)
        else:
            return new_poly(coefficients, num)
    return helper


calculator_old = calculator_generator((1, 2, 3, 4, 5), 'old')
calculator_new = calculator_generator((1, 2, 3, 4, 5), 'new')
calculator_old_1 = calculator_generator((1, 0, 10), 'old')
calculator_new_1 = calculator_generator((), 'new')


print(calculator_old(3))
print(calculator_new(3))
print(calculator_old_1(5))
print(calculator_new_1(25))

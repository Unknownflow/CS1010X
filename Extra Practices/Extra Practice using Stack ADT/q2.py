def make_postfix(expr):
    def helper(expr):
        if type(expr[0]) == tuple and type(expr[2]) == tuple:
            return helper(expr[0]) + helper(expr[2]) + (expr[1],)
        elif type(expr[0]) == tuple:
            return helper(expr[0]) + (expr[2], expr[1])
        elif type(expr[2]) == tuple:
            return (expr[0],) + helper(expr[2]) + (expr[1],)
        else:
            return (expr[0], expr[2], expr[1])

    return helper(expr)


print(make_postfix((1, '+', 2)))
print(make_postfix(((1, '+', 2), '*', 3)))
print(make_postfix((3, '*', (1, '+', 2))))
print(make_postfix((12, '+', 34)))
print(make_postfix(((1, '+', 2), '*', (3, "-", 4))))

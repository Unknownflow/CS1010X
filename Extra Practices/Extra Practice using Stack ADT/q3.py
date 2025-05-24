def make_postfix(expr):
    def helper(expr):
        if type(expr[0]) == tuple and type(expr[-1]) == tuple:
            return helper(expr[0]) + helper(expr[-1]) + (expr[1],)
        elif type(expr[0]) == tuple:
            return helper(expr[0]) + (expr[-1], expr[1])
        elif type(expr[-1]) == tuple:
            return (expr[0],) + helper(expr[-1]) + (expr[1],)
        else:
            return (expr[0], expr[2], expr[1])

    return helper(expr)


print(make_postfix((1, '?', 2, ':', 3)))
print(make_postfix((3, '^', 2)))
print(make_postfix(((1, '+', 2), '?', 4, ':', (2, '^', (3, '?', 6, ':', 2)))))

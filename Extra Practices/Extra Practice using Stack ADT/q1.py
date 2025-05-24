def make_empty_stack():
    return []


def make_stack(seq):
    stack = []
    for val in seq:
        stack.append(val)
    return stack


def is_empty_stack(stack):
    return len(stack) == 0


def peek_stack(stack):
    return stack[-1]


def push_stack(stack, item):
    stack.append(item)


def pop_stack(stack):
    return stack.pop()


def clear_stack(stack):
    while stack:
        stack.pop()


def calculate(inputs):
    # you may assume that the input is always valid, i.e. you do not need to
    # check that the stack has at least 2 elements if you encounter an operator
    stack = make_empty_stack()

    for input in inputs:
        if input in ["+", "-", "*", "/"]:
            right = pop_stack(stack)
            left = pop_stack(stack)
            res = 0

            if input == "+":
                res = left + right
            elif input == "-":
                res = left - right
            elif input == "*":
                res = left * right
            elif input == "/":
                res = left / right
            push_stack(stack, res)
        else:
            push_stack(stack, input)

    return peek_stack(stack)


print(calculate((1, 2, '+', 3, '*')))
print(calculate((1, 2, '+')))
print(calculate((1, 25, '+', 3, '*')))
print(calculate((3, 1, 2, '+', '*')))
print(calculate((28, )))
print(calculate((1, 2, '+', 3, '/')))
print(calculate((5, 2, '/', 4, '*')))
print(calculate((1, 2, '*', 3, '-', 2, '*', 5, '+')))
print(calculate((5, 1, 20, 2, '+', 23, 12, '-', '/', '+', '*')))

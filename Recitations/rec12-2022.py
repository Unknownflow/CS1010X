from math import *


def deep_reverse(a):
    if a == []:
        return []
    elif type(a[0]) == list:
        print("list", a, a[0], a[1:])
        return deep_reverse(a[1:]) + [deep_reverse(a[0])]
    else:
        print("xx", a, a[0], a[1:])
        return deep_reverse(a[1:]) + [a[0]]


# print(deep_reverse([1, 2, [3, 4, [5, 6]]]))


def deep_sum(a):
    if a == []:
        return 0
    elif type(a[0]) == list:
        print("list", a, a[0], a[1:])
        return deep_sum(a[1:]) + [deep_sum(a[0])]
    else:
        print("xx", a, a[0], a[1:])
        return deep_sum(a[1:]) + a[0]

# Q2 a


def make_stack():
    stuff = []

    def helper(msg, *arg):
        if msg == "is_empty":
            return stuff == []
        elif msg == "push":
            stuff.extend(arg)
        elif msg == "peek":
            return stuff[-1]
        elif msg == "pop":
            if len(stuff) >= 1:
                return stuff.pop()   # cannot put stuff = stuff...become local.
            else:
                return None
        elif msg == 'size':
            return len(stuff)
        elif msg == 'print':
            print("stack has:", stuff)
        else:
            print("unknown")

    return helper


def prefix_infix(a):
    op_s = make_stack()
    for op in a:
        if op in ['*', '/', '+', '-'] or op_s("peek") in ['*', '/', '+', '-']:
            # print("op:", op)
            op_s("push", str(op))  # not enough parameters to do the operation
        else:  # op_s("peek") not in ['*', '/', '+', '-']:
            # first pop must be a number, and the second must be an operator
            op_s("push", "(" + op_s("pop") + op_s("pop") + str(op) + ")")
            # print(op_s("peek"))
            # missing here....
            # some while loop needed to pop out and push back more....
            # op_s("print")

            while op_s("size") >= 3:
                op1 = op_s("pop")
                op2 = op_s("pop")
                op3 = op_s("pop")
                if op3 in ['*', '/', '+', '-'] and op2 not in ['*', '/', '+', '-']:
                    op_s("push", "(" + op2 + op3 + op1 + ")")
                else:
                    op_s("push", op3)
                    op_s("push", op2)
                    op_s("push", op1)
                    break

    # op_s("print")
    # print("=== end of for loop===")
    while op_s("size") > 2:
        # print(op_s("size"))
        back = op_s("pop")
        front = op_s("pop")
        # print("b:", back, "f:", front, op_s("peek"))
        op_s("push", "(" + front + op_s("pop") + back + ")")
    return op_s("pop")


# print("correct for this case:", prefix_infix(['+', '*', 5, 4, '-', 2, 1]))
# print("wrong ans1:", prefix_infix(['-', '+', '*', 5, 4, '-', 2, 1, 8]))
# print("wrong ans2:", prefix_infix(['-', '+', '*', 5, 4, 2, 1]))


def enumerate_interval(min, max):
    return list(range(min, max+1))


def map(fn, seq):
    if seq == []:
        return []
    else:
        return [fn(seq[0]),] + map(fn, seq[1:])


def filter(pred, seq):
    if seq == []:
        return []
    elif pred(seq[0]):
        return [seq[0],] + filter(pred, seq[1:])
    else:
        return filter(pred, seq[1:])


def accumulate(fn, initial, seq):
    if seq == []:
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))


# print(enumerate_interval(1, 8))
# print(map(lambda x: 5*x, enumerate_interval(1, 12)))
# print(map(lambda x: x*x, filter(lambda x: x % 2, enumerate_interval(1, 12))))
# print(map(lambda x: x*x if x % 2 else x//2, enumerate_interval(1, 10)))
# print(accumulate(lambda x, y: y+[x], [], map(lambda x: x*2,
#       filter(lambda x: x % 3 != 0, enumerate_interval(1, 10)))))

# observe that i often have debugging stuff


def power_set(a):
    if a == []:
        return [[]]  # important cannot be []
    else:
        result1 = power_set(a[1:])
        # print("r1: ", result1)
        # need the "list", else object
        result2 = list(map(lambda x: x + [a[0]], result1))
        # print("a[0]: ", a[0], "r2:", result2)
        return result2 + result1


# print(power_set([1, 2, 3]))

# planning that I do .... reminder to you on how you should solve your PE too.
# check the size .....the size has to be 2^n
# take the largest set in the input to generate our powerset, called ps
# check that each item in the ps is in the input
# ......make sure you sort each items in the input, and each item in the ps


def power_set_check(a):
    size = int(log(len(a), 2))
    print("size", size)
    if 2**size != len(a):
        return False
    check = []
    for i in a:
        print("i:", i)
        if len(i) == size:
            print("checking")
            check = power_set(i)
            print("after generation", check)
            break
    print("xx:", check)
    for j in a:
        print("before j:", j)
        j.sort()   # needed
        print("after j:", j)

    for i in check:     # the alternative of taking the input to check with our generated powerset - this is wrong
        print("before i:", i)
        i.sort()   # needed
        print("after i:", i)
        if i not in a:
            print("cur i", i)
            return False
    return True

# OOP ....PE....also, incremental development.


# print(power_set_check([[3, 2, 1], [2, 1], [3, 1], [1], [3, 2], [2], [3], []]))


class Number(object):
    def __init__(self, num):
        self.num = num

    def value(self):
        return self.num

    def minus(self, amt):
        if self.value() == "Undefined" or amt.value() == "Undefined":
            return (Number("Undefined"))
        return Number(self.value() - amt.value())

    def plus(self, amt):
        if self.value() == "Undefined" or amt.value() == "Undefined":
            return (Number("Undefined"))
        return Number(self.value() + amt.value())

    def times(self, amt):
        if self.value() == "Undefined" or amt.value() == "Undefined":
            return (Number("Undefined"))

        return Number(self.value() * amt.value())

    def divide(self, amt):
        if self.value() == "Undefined" or amt.value() == "Undefined":
            return (Number("Undefined"))
        if (amt.value() == 0):
            return (Number("Undefined"))
        return Number(self.value() / amt.value())

print("=========== Q1 =======")
################# Q1
def deep_reverse(a):
    if a==[]:
        return []
    elif type(a[0]) == list:
        return deep_reverse(a[1:]) + [ deep_reverse(a[0]) ]
    else:
        return deep_reverse(a[1:]) + [a[0]]

print(deep_reverse([1, 2,[3, 4], [[5]], [6, [7, 8], 9]]))

def deep_sum(a):
    if a==[]:
        return 0
    elif type(a[0]) == list:
        return deep_sum(a[1:]) +  deep_sum(a[0]) 
    else:
        return deep_sum(a[1:]) + a[0]

print(deep_sum([1, 2,[3, 4], [[5]], [6, [7, 8], 9]]))


##############################################################


print("=========== Q2 =======")
################# Q2
# prefix infix
def make_stack():
    stuff = []
    def helper(msg, *arg):
        if msg == "is_empty":
            return stuff == []
        elif msg=="push":
            stuff.extend(arg) 
        elif msg=="peek":
            return stuff[-1]
        elif msg=="pop":
            if len(stuff) >= 1:
                return stuff.pop()   # cannot put stuff = stuff...become local.
            else:
                return None
        elif msg=='size':
            return len(stuff)
        elif msg=='print':
            print("stack has:", stuff)
        else:
            print("unknown")
            
    return helper

stk = make_stack()
stk("push", 1)
stk("push", 2)
stk("push", 3)
stk("peek")
stk("pop")
stk("peek")
stk("size")

#####
def prefix_infix(a):
    stack = make_stack()
    # consuming the input symbol one by one in a
    for op in a:
        if op in ["*", "/", "+", "-"]:
            stack("push", str(op))
        elif stack("peek") in ["*", "/", "+", "-"]:
            stack("push", str(op))
        else:
            temp = "(" + stack("pop") + stack("pop") + str(op)+ ")"
            while stack("size")>0 and stack("peek") not in ["*", "/", "+", "-"]:
                temp = "(" + stack("pop") + stack("pop") + temp + ")"
            stack("push", temp)
            
    stack("print")
    while stack("size") > 1:
        back = stack("pop")
        front = stack("pop")
        stack("push", "(" + front + stack("pop") + back+ ")")
    return stack("pop") 

print( prefix_infix (['+', '*', 5, 4, '-', 2, 1]))
print( prefix_infix (["-", '+', '*', 5, 4, 2, 1]))
print( prefix_infix (["-", '+', '*', 5, 4, "-", 2, 1, 8]))

####################################################################
#### Q3
print("=========== Q3 =======")


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

print( enumerate_interval(1, 8) )
print( map(lambda x: x*5, enumerate_interval(1, 12) ))

print( map(lambda x:x*x, filter(lambda x: x%2, enumerate_interval(1, 11) )))

print( map(lambda x: x*x if x%2 else x//2, enumerate_interval(1, 10) ))

print( accumulate(lambda x,y: y + [x], [], filter(lambda x: x%2==0 and x%6!=0, enumerate_interval(1, 20))))

#######################
print("=========== Q4 =======")


def power_set(a):
    if a==[]:
        return [[]]
    else:
        result1 = power_set(a[1:])
        result2 = map(lambda x: x+[a[0]], result1)
        return result1 + result2

A = power_set(["1", "2", "3"])
#A = A + [ ["a"] ]
print(A)

from math import *
def power_set_check(a):
    size = int(log(len(a),2))
    print(size)
    if 2**size != len(a):
        return False

    for i in a:
        if len(i) == size:
            check = power_set(i)
            break

    print("check", check)

    for j in a:
        j.sort()

    for i in check:
        #i.sort()
        if i not in a:
            return False
    return True

print(power_set_check(A))

#####
print("=========== Q5 =======")

class Number(object):
        def __init__(self, num):
           self.num = num

        def value(self):
            return self.num

        def minus(self, amt):
            if self.value() == "Undefined" or amt.value() == "Undefined":
                return Number("Undefined")
            return Number(self.value() - amt.value())
        
        def plus(self, amt):
            if self.value() == "Undefined" or amt.value() == "Undefined":
                return Number("Undefined")
            return Number(self.value() + amt.value())

        def times(self, amt):
            if self.value() == "Undefined" or amt.value() == "Undefined":
                return Number("Undefined")
            return Number(self.value() *  amt.value())

        def divides(self, amt):
            if self.value() == "Undefined" or amt.value() == "Undefined":
                return Number("Undefined")
            elif amt.value() == 0:
                return Number("Undefined")
            else:
                return Number(self.value() /  amt.value())


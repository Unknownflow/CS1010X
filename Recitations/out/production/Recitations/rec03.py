# Python Q1
function = lambda params: expression

# Problems 
# Q1a - 17

x = 2
def f():
    x = 5
    y = x + 5
    return x + y

# print('Q1a', f() + x)

# Q1b - 18

x = 2
y = 3
def g(x):
    y = x + 5
    x = 7
    return x + y

# print('Q1b', g(y)+ y)

# Q1c - 4

x = 4
def foo(x):
    return x(3)

# print('Q1c', foo(lambda x: x+1))

# Q1d - 16

x = 5
def bar(x, y):
    return y(x)

# print('Q1d', bar(4, lambda x: x ** 2))

# Q2

# Iterative
# Time Complexity: O(n)
# Space Complexity: O(1)
def my_sum(n):
    result = 0

    for i in range(1, n+1):
        result += i * (i+1)
      
    return result

# Test cases
# for i in range(1, 10):
#     print('Q2', my_sum(i))


# Recursive
# Time complexity: O(n)
# Space complexity: O(n)
def my_sum(n):
    if n == 1:
        return 2
    else:
        return n * (n+1) + my_sum(n-1)

# Test cases
# for i in range(1, 10):
#     print('Q2', my_sum(i))

def sum(term, a, next, b):
    if a > b:
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)

# Q5
# T1: lambda x: x * (x+1)
# T2: 1
# T3: lambda x: x+1
# T4: n 

def my_sum(n):
    return sum(lambda x: x * (x+1), 1, lambda x: x+1, n)

# Test cases
# for i in range(1, 10):
#     print('Q5', my_sum(i))

def fold(op, f, n):
    if n == 0:
        return f(0)
    else:
        return op(f(n), fold(op, f, n-1))

# Q6
# T1: lambda x, y: x+y
# T2: lambda x: x * (x+1)
# T3: n
def my_sum(n):
    return fold(lambda x, y: x+y, lambda x: x * (x+1), n)

# Test cases
# for i in range(1, 10):
#     print('Q6', my_sum(i))

# Q7 Iterative sum
def sum(term, a, next, b):
    result = 0

    while a <= b:
        result += term(a)
        a = next(a)
    
    return result

# for i in range(1, 10):
#     print('Q7', sum(lambda x: x * (x+1), 1, lambda x: x+1, i))

# Q8 Iterative fold -- need to work for non associative like - and / also
# def fold_iter(op, f, n):
#     result = f(0)

#     while n > 0:
#         result = op(f(n), result)
#         n -= 1
    
#     return result

def fold_iter(op, f, n):
    result = f(0)
    curr = 1

    while curr <= n:
        result = op(f(curr), result)
        curr += 1 
    
    return result

def fold(op, f, n):
    result = f(0)
    for i in range(1, n+1):
        result = op(f(i), result)
    return result

for i in range(1, 10):
    print('Q8', fold(lambda x, y: x+y, lambda x: x * (x+1), i))
    print('Q8', fold_iter(lambda x, y: x+y, lambda x: x * (x+1), i))
    print('Q8', fold(lambda x, y: x-y, lambda x: x * (x+1), i))
    print('Q8', fold_iter(lambda x, y: x-y, lambda x: x * (x+1), i))
    print('Q8', fold(lambda x, y: (x+1)/(y+1), lambda x: x * (x+1), i))
    print('Q8', fold_iter(lambda x, y: (x+1)/(y+1), lambda x: x * (x+1), i))
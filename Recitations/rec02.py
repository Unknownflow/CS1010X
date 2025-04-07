from rec01 import *

# Q1a
# Write a recursive function called order_size which takes an order and returns
# the number of combos in the order. For example, order_size(237) -> 3
def order_size(order):
  if order == empty_order():
    return 0
  else:
    return 1 + order_size(order//10)

print(order_size(237))
print(order_size(123456789))


# Q1b
# Write an iterative version of order_size.
def order_size(order):
  count = 0 

  while order > empty_order():
    order //= 10
    count += 1
  
  return count

print(order_size(237))
print(order_size(123456789))


# Q1c
# Write a recursive function called order_cost which takes an order and returns
# the total cost of all the combos
def order_cost(order):
  if order == empty_order():
    return 0
  else:
    return combo_price(order%10) + order_cost(order//10)
  
print(order_cost(2367))
print(order_cost(8888))
print(order_cost(12345678))


# Q1d
# Write an iterative version of order_cost.
def order_cost(order):
  total_cost = 0

  while order > empty_order():
    combo = order % 10
    total_cost += combo_price(combo)
    order //= 10
  
  return total_cost

print(order_cost(2367))
print(order_cost(8888))
print(order_cost(12345678))


# Q1e
# Homework: Write a function called add_orders which takes two orders and re-
# turns a new order that is the combination of the two. For example, add_orders
# (123,234) -> 123234. Note that the order of the combos in the new order is not
# important as long as the new order contains the correct combos. add_orders(123,234)
# -> 122334 would also be acceptable.
def add_orders(order_one, order_two):
  new_order = order_one

  while order_two > empty_order():
    combo = order_two % 10
    new_order = new_order * 10 + combo
    order_two //= 10
  
  return new_order

print(add_orders(123, 234))

# Q2 Give order notation for the following
# a) 5n^2 + n --> n^2
# 5n^2 + n < 5n^2 + n^2 when n > 1
#          = 6n^2
#          = O(n^2) because we can choose k = 7, n_0 = 1

# b) n^(1/2) + n --> n
# n^(1/2) + n < n + n for n > 1
#             = 2n
#             = O(n) where k = 3, n_0 = 1

# c) (3^n)(n^2) --> (3^n)(n^2) for k = 1 and n_0 = 1
# 3^n n^2 < 4 ^ n (you can find a fixed n_0 such that 3^n n^2 < 4^n for all n > n_0)
#         = O(4^n) ..... I dont like this
#         < O(100^n)
#         < O(10000000^n)

# Q3
# def fact(n):
#   if n == 0:
#     return 1
#   else :
#     return n * fact(n - 1)
# Running time: O(n)
# Space: O(n)

# assume time complexity of +-*/ as O(1)

# Q4 Write an iterative version of fact
def fact(n):
  result = 1

  for i in range(2, n+1):
    result *= i
  
  return result

print(fact(1))
print(fact(3))
print(fact(5))

# Q5
# def find_e(n):
#   if n == 0:
#     return 1
#   else:
#     return 1/fact(n) + find_e(n-1)
# Running time: O(n^2)
# Space: O(n)

# Q6
# Assume you have a function is_divisible(n, x) which returns True if n is divisible
# by x. It runs in O(n) time and O(1) space. Write a function is_prime which takes a
# number and returns True if it’s prime and False otherwise.
from math import sqrt

def is_divsible(n, x):
  if n % x == 0:
    return True
  else:
    return False
  
def is_prime(n):
  if n <= 1:
    return False
  if n == 2:
    return True
  if is_divsible(n, 2):
    return False
  for i in range(3, int(sqrt(n))+1):
    if is_divsible(n, i):
      return False
    
  return True

# is_divisible(n, x) has a O(n) time and O(1) space
# Running time: O(n^(3/2))
# Space: O(1)
for i in range(0, 15):
  print(is_prime(i), i)

# Q7: Homework: Write an iterative version of find_e
# use the iterative version of fact(n)
def find_e_iterative(n):
  result = 0

  for i in range(n+1):
    result += 1/fact(i)
  
  return result

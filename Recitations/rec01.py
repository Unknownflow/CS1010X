# Q3a
# Write a function called biggie_size which when given a regular combo returns
# a biggie_sized version.
def biggie_size(size):
  return size + 4


print(biggie_size(1))
print(biggie_size(2))
print(biggie_size(3))
print(biggie_size(4))


# Q3b
# Write a function called unbiggie_size which when given a biggie_sized combo
# returns a non-biggie_sized version
def unbiggie_size(size):
  return size - 4


print(unbiggie_size(5))
print(unbiggie_size(6))
print(unbiggie_size(7))
print(unbiggie_size(8))


# Q3c
# Write a function called is_biggie_size which when given a combo, returns True
# if the combo has been biggie_sized and False otherwise.
def is_biggie_size(size):
  if size >= 5:
    return True
  else:
    return False

print(is_biggie_size(1))
print(is_biggie_size(4))
print(is_biggie_size(5))
print(is_biggie_size(8))

# Q3d
# Write a function called combo_price which takes a combo and returns the price
# of the combo. Each patty costs $1.17, and a biggie_sized version costs $.50
# extra overall.
def combo_price(combo):
  patty_price = 1.17
  extra_cost = 0.5

  if is_biggie_size(combo):
    return patty_price * unbiggie_size(combo) + extra_cost
  else:
    return patty_price * combo
  
print(combo_price(1))
print(combo_price(4))
print(combo_price(5))
print(combo_price(8))


# Q3e
# An order is a collection of combos. We’ll encode an order as each digit rep-
# resenting a combo. For example, the order 237 represents a Double, Triple,
# and biggie_sized Triple. Write a function called empty_order which takes no
# arguments and returns an empty order which is represented by 0
def empty_order():
  return 0


print(empty_order())

# Q3f
# Write a function called add_to_order which takes an order and a combo and
# returns a new order which contains the contents of the old order and the new
# combo. For example, add_to_order(1,2) -> 12
def add_to_order(order, combo):
  new_order = order * 10 + combo
  return new_order


print(add_to_order(1,2))
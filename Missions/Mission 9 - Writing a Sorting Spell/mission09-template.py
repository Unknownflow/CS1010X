#
# CS1010X --- Programming Methodology
#
# Mission 9 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###############
# Pre-defined #
###############

a = [6, 4, 2, 9, 10, 4, 2, 1, 3]

###################
# Helper function #
###################

def accumulate(fn, initial, seq):
    if not seq: # if seq is empty
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))

###########
# Task 1a #
###########

# The enumerate function should be helpful for you here.
# It takes in a sequence (either a list or a tuple)
# and returns an iteration of pairs each of which
# contains the index of the element and the element itself.
# Here's how to use it.

# for i, elem in enumerate((4, 10, 1, 3)):
#     print("I am in the", i ,"position and I am", elem)
# 
# I am in the 0 position and I am 4
# I am in the 1 position and I am 10
# I am in the 2 position and I am 1
# I am in the 3 position and I am 3

def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    
    return len(seq)

print("## Q1a ##")
print(search(-5, (1, 5, 10)))
# => 0
print(search(3, (1, 5, 10)))
# => 1
print(search(7, [1, 5, 10]))
# => 2
print(search(5, (1, 5, 10)))
# => 1
print(search(42, [1, 5, 10]))
# => 3
print(search(42, (-5, 1, 3, 5, 7, 10)))
# => 6

###########
# Task 1b #
###########

def binary_search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted.
    Uses O(lg n) time complexity algorithm."""
    if len(seq) == 0:
        return 0
    
    left = 0
    right = len(seq) - 1

    while left <= right:
        mid = (left + right) // 2 # get mid pos
        if x == seq[mid]: # insertion pt found
            return mid
        elif x < seq[mid]: # shift right ptr to mid - 1
            right = mid - 1
        else: # shift left ptr to mid + 1
            left = mid + 1

    return left

print("## Q1b ##")
print(binary_search(-5, (1, 5, 10)))
# => 0
print(binary_search(3, (1, 5, 10)))
# => 1
print(binary_search(7, [1, 5, 10]))
# => 2
print(binary_search(5, (1, 5, 10)))
# => 1
print(binary_search(42, [1, 5, 10]))
# => 3
print(binary_search(42, (-5, 1, 3, 5, 7, 10)))
# => 6

###########
# Task 2a #
###########

def insert_list(x, lst):
    """ Inserts element x into list lst such that x is less than or equal
        to the next element and returns the resulting list."""
    pos = search(x, lst)
    lst.insert(pos, x)
    return lst

print("## Q2a ##")
print(insert_list(2, [1, 5, 9]))
#=> [1, 2, 5, 9]
print(insert_list(10, [1, 5, 9]))
#=> [1, 5, 9, 10]
print(insert_list(5, [2, 6, 8]))
#=> [2, 5, 6, 8]

###########
# Task 2b #
###########

def insert_tup(x, tup):
    """ Inserts element x into tuple tup such that x is less than or equal
        to the next element and returns the resulting tuple."""
    pos = search(x, tup)
    return tup[:pos] + (x, ) + tup[pos:]

print("## Q2b ##")
print(insert_tup(2, (1, 5, 9)))
#=> (1, 2, 5, 9)
print(insert_tup(10, (1, 5, 9)))
#=> (1, 5, 9, 10)
print(insert_tup(5, (2, 6, 8)))
#=> (2, 5, 6, 8)

###########
# Task 2c #
###########

tup = (5, 4, 10)
output_tup = insert_tup(7, tup)
lst = [5, 4, 10]
output_lst = insert_list(7, lst)

# print(tup is output_tup)
#=> Output: False
# print(tup == output_tup)
#=> Output: False

# print(lst is output_lst)
#=> Output: True
# print(lst == output_lst)
#=> Output: True

#=> Explain the outputs:
#=> Since tuple is immutable, a new tuple is needed to be created when trying to
#=> insert a new element into the tuple. The new tuple will be created at
#=> another memory address, and thus the new tuple will have a differnt identity
#=> compared to the original tuple and the is statement is false. The new tuple 
#=> will also have the new element in it while the original tuple will not,
#=> hence they are not equivalent and the == statement is false.
#=> 
#=> Since question 2a requires us to insert the item into the input list itself,
#=> the original list is thus returned from the insert_list function, hence
#=> both list will point to the same memory address and will have the same
#=> identity and the is statement is true. The two list will also be equivalent
#=> to each other, thus the == statement is true.


###########
# Task 3a #
###########

def sort_list(lst):
    """ Sorts list lst in ascending order."""
    new_lst = []

    for i in range(len(lst)):
        elem = lst[i]
        insert_list(elem, new_lst)
    
    return new_lst

print("## Q3a ##")
print(sort_list([9, 6, 2, 4, 5]))
#=> [2, 4, 5, 6, 9]
print(sort_list([42, 7, 6, -42, 0]))
#=> [-42, 0, 6, 7, 42]
print(sort_list(["soda", "cola", "sprite", "root beer", "apple cider"]))
#=> ['apple cider', 'cola', 'root beer', 'soda', 'sprite']
print(sort_list(["turtle", "penguin", "dog", "cat", "ant eater", "butterfly"]))
#=> ['ant eater', 'butterfly', 'cat', 'dog', 'penguin', 'turtle']

###########
# Task 3b #
###########

#=> Time complexity of sort_list: O(n**2)

###########
# Task 3c #
###########

def sort_tup(tup):
    """ Sorts tuple tup in an ascending order."""
    new_tup = ()

    for i in range(len(tup)):
        elem = tup[i]
        new_tup = accumulate(insert_tup, new_tup, (elem, ))

    return new_tup

print("## Q3c ##")
print(sort_tup((9, 6, 2, 4, 5)))
#=> (2, 4, 5, 6, 9)
print(sort_tup((42, 7, 6, -42, 0)))
#=> (-42, 0, 6, 7, 42)
print(sort_tup(("soda", "cola", "sprite", "root beer", "apple cider")))
#=> ('apple cider', 'cola', 'root beer', 'soda', 'sprite')
print(sort_tup(("turtle", "penguin", "dog", "cat", "ant eater", "butterfly")))
#=> ('ant eater', 'butterfly', 'cat', 'dog', 'penguin', 'turtle')

###########
# Task 4a #
###########

import shelf

# Please uncomment the test function calls to see the animation

def insert_animate(block_pos, shelf, high):
    """
    Pops the block at block_pos and inserts it in the position in the shelf
    such that its size is less than or equal to the one succeeding it. It searches
    for this position within zero and high.

    NOTE: To actually see the animation, please uncomment the testing function
    below.
    """
    # optional to return shelf but we do this for debugging
    block = shelf.pop(block_pos)

    for i in range(high):
        if block.size <= shelf[i].size:
            shelf.insert(i, block)
            return shelf
    
    shelf.insert(high, block)
    return shelf

# Test cases for insert_animate

def test_insert_animate():
    shelf.clear_window()
    s = shelf.init_shelf((2, 6, 1, 4, 8, 3, 9))
    print("## Q4a ##")
    print(insert_animate(0, s, 0))
    # => [Block size: 2, Block size: 6, Block size: 1, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(1, s, 1))
    # => [Block size: 2, Block size: 6, Block size: 1, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(2, s, 2))
    # => [Block size: 1, Block size: 2, Block size: 6, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(3, s, 3))
    # => [Block size: 1, Block size: 2, Block size: 4, Block size: 6, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(6, s, 6))
    # => [Block size: 1, Block size: 2, Block size: 4, Block size: 6, Block size: 8, Block size: 3, Block size: 9]

    s = shelf . init_shelf ((5 , 2 , 4 , 1 ))
    print ( insert_animate (1 , s , 1 ))
    # [ Block size : 2 , Block size : 5 , Block size : 4 , Block size : 1]
    print ( insert_animate (3 , s , 3 ))
    # [ Block size : 1 , Block size : 2 , Block size : 5 , Block size : 4]

# Uncomment function call to test insert_animate()
# test_insert_animate()

###########
# Task 4b #
###########

def sort_me_animate(shelf):
    """
    Maintains a sorted portion and inserts every block in the shelf into the
    sorted portion.

    NOTE: To actually see the animation, please uncomment the testing function
    below.

    """
    # optional to return shelf but we do this for debugging
    for i in range(1, len(shelf)):
        insert_animate(i, shelf, i) # not inclusive of high (2nd i)
    return shelf

# Test cases for sort_me_animate

def test_sort_me_animate():
    shelf.clear_window()
    s = shelf.init_shelf((5,2,6,9,1,4,8,3))
    print("## Q4b ##")
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 2, Block size: 3, Block size: 4, Block size: 5, Block size: 6, Block size: 8, Block size: 9]
    shelf.clear_window()
    s = shelf.init_shelf((4, 8, 2, 9, 3, 1, 2, 3, 4, 10, 7, 5, 6))
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 2, Block size: 2, Block size: 3, Block size: 3, Block size: 4, Block size: 4, Block size: 5, Block size: 6, Block size: 7, Block size: 8, Block size: 9, Block size: 10]

# Test case to catch mutation while sorting

def test_sort_me_with_duplicates():
    shelf.clear_window()
    s = shelf.init_shelf((1,3,4,1,3,2))
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 1, Block size: 2, Block size: 3, Block size: 3, Block size: 4]

# Uncomment function call to test sort_me_animate()
test_sort_me_animate()
# test_sort_me_with_duplicates()

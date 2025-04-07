#
# CS1010X --- Programming Methodology
#
# Mission 11a
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <your collaborator's matric> <your collaborator's name>

###############
# Mission 11a #
###############

##########
# Task 1 #
##########

# With these operations, compound generic operations can be defined, such as
# def square(x):
#   return mul(x, x)

# (a) What are the types of the input and output of the generic square operation?
# Answer: (Generic-Num) -> (Generic-Num)

# (b) Why would we prefer to define square in the above way, rather than:
# def square(x):
#    return apply_generic("square", x)
# Answer: More work is needed for the programmer to define square for the different number packages as square function will
# be needed to be added into the operations table for each number package when applying generic to square instead of using mul(x,x).

##########
# Task 2 #
##########
# In the ordinary number package, a generic number operator is indexed by the
# name of the operator and a tuple of strings. For example, the add operator is
# indexed by ’add_ord’ and (’ordinary’, ’ordinary’); negation is indexed by
# ’negate_ord’ and (’ordinary’, ).
# In contrast, the constructor that creates an ordinary number is indexed by
# ’make_ord’ and just a string ’ordinary’. Explain why we have such a difference.

# 
 
# Hint: Consider the differences in the process of the creation of a Generic-Num,
# such as create_ordinary, and the operations we can apply on Generic-Num, such
# as add. How is make_ord invoked, and how is add_ord invoked?

# Answer: 

# Below is the process of execution of the function create_ordinary
# create_ordinary(x)
# -> get("make", "ordinary")(x)
# --> _operations_table["make"]["ordinary"](x)
# ---> make_ord(x) 
# ----> tag(x)
# -----> attach_tag("ordinary", x)
# ------> ("ordinary", x)

# Below is the process of execution of the function add, where x and y have the ordinary tag
# add(x, y)
# -> apply_generic("add", x, y)
# --> get("add", ("ordinary", "ordinary"))(x, y)
# ---> _operations_table["add"][("ordinary", "ordinary")](x, y)
# ----> add_ord(x, y)
# -----> make_ord(x + y)
# ------> tag(x+y)
# -------> attach_tag("ordinary", x+y)
# --------> ("ordinary", x+y)

# From the execution of create_ordinary(x), we can see that add_ord is invoked when
# looking for the entry in "add" and ("ordinary", "ordinary") in the operations table 
# while make_ord is invoked when looking for the entry in "make" and "ordinary" in
# the operations table. 

# There is such a difference due to the additional apply_generic function found in 
# add and not create_ordinary. The apply_generic function takes in an operator and 
# a variable number of arguments and a tuple of type tags is generated from the 
# variable number of arguments (type_tags = tuple(map(type_tag, args))). 

# This tuple is used in the second argument for the get function get("add", ("ordinary", "ordinary")).
# This get function will return a operations table lookup with "add" (an operator) and
# ("ordinary", "ordinary") (a tuple of strings), which retrieves the add operator. 

# Since all the generic operators calls the apply_generic function, a generic number 
# operator is thus indexed by the name of the operator and a tuple of strings. 

# For constructors, since the apply_generic function is not called, the a tuple of strings
# is not created and a string like "ordinary" will thus be used to index for the make 
# function in the oeprations table.

##########
# Task 3 #
##########

# There’s a right way and a wrong way to create a generic rational number. Here are two tries at
# producing 9/10. Which is the right way?

from generic_arith import create_rational, create_ordinary
first_try = create_rational(9, 10)
second_try = create_rational(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce 9/10 and 3/10 and then try to add
# them? Why does this happen?

# Right way: second_try
# What happens: An error message is produced -> Exception: ('Bad tagged datum -- type_tag ', 9)
# Why it happens: The first try passes in a python integer and does not pass a generic ordinary number into its arguments 
# and a generic rational number can only be formed with generic ordinary numbers as its numerator and denominator. This would 
# thus result in an error when trying to add 2 rational numbers together with the first implementation.

##########
# Task 4 #
##########

# Produce expressions that define r2_7 to be the generic rational number whose numerator part is
# 2 and whose denominator part is 7, and r3_1 to be the generic rational number whose numerator
# is 3 and whose denominator is 1. Assume that the expression
# >>> csq = square(sub(r2_7, r3_1))
# is evaluated. Draw a box and pointer diagram that represents csq.

# As an example, the following is a box and pointer diagram that represents x, a Generic-
# Ord number:
# x = create_ordinary(5)
#
#         +---+---+---+---+
# x  -->  |       |       |
#         +---+---+---+---+
#             |       |
#             v       v
#         "ordinary"  5

# FILL IN YOUR ANSWERS HERE:
r2_7 = create_rational(create_ordinary(2), create_ordinary(7))
r3_1 = create_rational(create_ordinary(3), create_ordinary(1))

# csq = square(sub(r2_7, r3_1))

## Sample ASCII box and pointer diagrams (with 2 components) for your convenience
##            +---+---+---+---+
##            |       |       |  -->
##            +---+---+---+---+
##                |
##                v

##            +---+---+---+---+
##            |       |       |
##            +---+---+---+---+
##                |       |
##                v       v

##########
# Task 5 #
##########

# Within the generic rational number package, the internal add_rat function
# handled the addition operation. Why is it not
# possible to name this function "add"?

# Answer: If this function is named "add", the add function inside make_rat will recursively call the add function and since there
# is no base case declared in the add function, it will result in a recursion error and it does not return the correct output of the
# addition of 2 rational numbers. Thus, it is not possible to name this function "add".

##########
# Task 6 #
##########

from generic_arith import *

# Modify install_rational_package, indicating clearly your modifications.
def install_rational_package():
    def make_rat(x, y):
        return tag(reprat(x, y))
    def reprat(x, y):
        return (x, y)
    def numer(x):
        return x[0]
    def denom(x):
        return x[1]
    def tag(x):
        return attach_tag("rational", x)

    # add, sub, mul, div: (RepRat, RepRat) -> Generic-Rat
    def add_rat(x, y):
        return make_rat( add(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def sub_rat(x, y):
        return make_rat( sub(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def mul_rat(x, y):
        return make_rat( mul(numer(x), numer(y)),
                         mul(denom(x), denom(y)) )
    def div_rat(x, y):
        return make_rat( mul(numer(x), denom(y)),
                         mul(denom(x), numer(y)) )
    
    def negate_rat(x): # (RepRat) -> Generic-Rat
        return make_rat( negate(numer(x)), denom(x) )
    
    def is_zero_rat(x): # (RepRat) -> Py-Bool
        numerator = numer(x)
        if is_zero(numerator):
            return True
        else:
            return False
        
    def is_eq_rat(x, y): # (RepRat, RepRat) -> Py-Bool
        result1 = div(numer(x), denom(x))
        result2 = div(numer(y), denom(y))

        if is_equal(result1, result2):
            return True
        else:
            return False
    
    put("make", "rational", make_rat)
    put("add", ("rational", "rational"), add_rat)
    put("sub", ("rational", "rational"), sub_rat)
    put("mul", ("rational", "rational"), mul_rat)
    put("div", ("rational", "rational"), div_rat)
    put("negate", ("rational",), negate_rat)
    put("is_zero", ("rational",), is_zero_rat)
    put("is_equal", ("rational", "rational"), is_eq_rat)


install_rational_package()

def create_rational(x, y):
    return get("make", "rational")(x, y)

# Change the values for the test variables below
r1_2 = create_rational(create_ordinary(1), create_ordinary(2))
r2_4 = create_rational(create_ordinary(2), create_ordinary(4))
r1_8 = create_rational(create_ordinary(1), create_ordinary(8))
r0_1 = create_rational(create_ordinary(0), create_ordinary(1))
# print(add(r1_2, r1_2))
# print(add(r2_4, r2_4))

print(r1_2)
print(r2_4)
print(r1_8)
print(negate(r1_2))
print(is_zero(r1_2))
print(is_zero(r0_1))
#################
# Do not change #
#################
def gradeThis():
    if is_equal(sub(r1_2, mul(r2_4, r1_2)), add(r1_8, r1_8)):
        print("Well done!")
    else:
        print("Please check your solution.")
gradeThis()

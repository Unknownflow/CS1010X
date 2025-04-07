#
# CS1010X --- Programming Methodology
#
# Mission 11b
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <your collaborator's matric> <your collaborator's name>

###############
# Mission 11b #
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

# There’s a right way and a wrong way to create a generic complex number. Here are two tries at
# producing 9+10i. Which is the right way?

from generic_arith import *

first_try = create_complex(9, 10)
second_try = create_complex(create_ordinary(9), create_ordinary(10))
three_ten = create_complex(3, 10)

# print(add(first_try, second_try))
# What happens when you use the wrong way to produce 9+10i and 3+10i and then try to add
# them? Why does this happen?

# Right way: second_try
# What happens: An error message is produced -> Exception: ('Bad tagged datum -- type_tag ', 9)
# Why it happens: The first try passes in a python integer and does not pass a generic ordinary number into its arguments 
# and a generic complex number can only be formed with generic ordinary numbers as its numerator and denominator. This would 
# thus result in an error when trying to add 2 complex numbers together with the first implementation.

##########
# Task 4 #
##########

# Produce expressions that define c2_plus_7i to be the generic complex number whose real part is 2
# and whose imaginary part is 7, and c3_plus_1i to be the generic complex number whose real part
# is 3 and whose imaginary part is 1. Assume that the expression
# >>> csq = square(sub(c2_plus_7i, c3_plus_1i))
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
c2_plus_7i = create_complex(create_ordinary(2), create_ordinary(7))
c3_plus_1i = create_complex(create_ordinary(3), create_ordinary(1))

# csq = square(sub(c2_plus_7i, c3_plus_1i))
print(add(c2_plus_7i, c3_plus_1i))
# print(csq)
## Sample ASCII box and pointer diagrams (with 2 components) for your convenience
##            +---+---+---+---+
##            |   |   |    ---|--->
##            +---+---+---+---+
##                |
##                v

##            +---+---+---+---+
##            |   |   |   |   |
##            +---+---+---+---+
##                |       |
##                v       v

##########
# Task 5 #
##########

# Within the generic complex number package, the internal add_com function
# handled the addition operation. Why is it not
# possible to name this function "add"?

# Answer: If this function is named "add", when using "add" and ("complex", "complex"),
# to index the operation table, generic add function will be called instead of the
# complex add function. The apply_generic function will be called on the arguments, 
# and get(op, type_tags) will keep returning "add" and ("complex", "complex"),
# which causes the add function to be called infinitely and with no base case declared,
# a recursion error occurs and an incorrect output is returned.


##########
# Task 6 #
##########

from generic_arith import *

# Modify install_complex_package, indicating clearly your modifications.
def install_complex_package():
    def make_com(x, y):
        return tag(repcom(x, y))
    def repcom(x, y):
        return (x, y)
    def real(x):
        return x[0]
    def imag(x):
        return x[1]
    def tag(x):
        return attach_tag("complex", x)

    # add, sub, mul, div: (RepCom, RepCom) -> Generic-Com
    def add_com(x, y):
        return make_com( add(real(x), real(y)),
                         add(imag(x), imag(y)) )
    def sub_com(x, y):
        return make_com( sub(real(x), real(y)),
                         sub(imag(x), imag(y)) )
    def mul_com(x, y):
        return make_com( sub(mul(real(x), real(y)),
                             mul(imag(x), imag(y))),
                         add(mul(real(x), imag(y)),
                             mul(real(y), imag(x))))
    def div_com(x, y):
        com_conj = content(complex_conjugate(y))
        x_times_com_conj = content(mul_com(x, com_conj))
        y_times_com_conj = content(mul_com(y, com_conj))
        return make_com( div(real(x_times_com_conj), real(y_times_com_conj)),
                         div(imag(x_times_com_conj), real(y_times_com_conj)))
    def complex_conjugate(x):
        return make_com(real(x), negate(imag(x)))

    def negate_com(x): # (RepCom) -> Generic-Com
        real_x = real(x)
        imag_x = imag(x)
        neg_com = make_com(negate(real_x), negate(imag_x))
        return neg_com

    
    def is_zero_com(x): # (RepCom) -> Py-Bool
        real_x = real(x)
        imag_x = imag(x)
        
        if is_zero(real_x) and is_zero(imag_x):
            return True
        else:
            return False
    
    def is_eq_com(x, y): # (RepCom, RepCom) -> Py-Bool
        real_x = real(x)
        imag_x = imag(x)
        real_y = real(y)
        imag_y = imag(y)

        if is_equal(real_x, real_y) and is_equal(imag_x, imag_y):
            return True
        else:
            return False

    put("make", "complex", make_com)
    put("add", ("complex", "complex"), add_com)
    put("sub", ("complex", "complex"), sub_com)
    put("mul", ("complex", "complex"), mul_com)
    put("div", ("complex", "complex"), div_com)
    put("negate", ("complex",), negate_com)
    put("is_zero", ("complex",), is_zero_com)
    put("is_equal", ("complex", "complex"), is_eq_com)

install_complex_package()

def create_complex(x,y):
    return get("make", "complex")(x, y)

# Change the values for the test variables below
c_neg3_plus_10i = create_complex(create_ordinary(-3), create_ordinary(10))
c1_plus_2i = create_complex(create_ordinary(1), create_ordinary(2))
c1_plus_3i = create_complex(create_ordinary(1), create_ordinary(3))

#################
# Do not change #
#################
def gradeThis():
    if is_equal(sub(c_neg3_plus_10i, mul(c1_plus_2i, c1_plus_3i)),
        add(c1_plus_2i, c1_plus_3i)):
        print("Well done!")
    else:
        print("Please check your solution.")
gradeThis()

r1_minus1 = create_complex(create_ordinary(1), create_ordinary(-1))
rminus1_1 = create_complex(create_ordinary(-1), create_ordinary(1))
rminus1_1 = negate(rminus1_1)
print(is_equal(r1_minus1, rminus1_1))
r0_0 = create_complex(create_ordinary(0), create_ordinary(0))
print(is_zero(r0_0))
print(is_zero(r1_minus1))
print(is_equal(r1_minus1, r0_0))
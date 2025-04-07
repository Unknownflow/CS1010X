#
# CS1010X --- Programming Methodology
#
# Mission 12
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <your collaborator's name>, <11a/11b>

from generic_arith_min import *

###########################
# Rational Number Package #
###########################

# Copy and paste the install_rational_package procedure from Mission
# 11a below and complete the tasks below for this mission.

def install_rational_package():

    # Copy and paste your Mission 11a solution below here:
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

    ###########
    # Task 1a #
    ###########
    def repord_to_reprat(x): # RepOrd -> RepRat
        return reprat(create_ordinary(x), create_ordinary(1))

    ###########
    # Task 2a #
    ###########
    def RRmethod_to_ORmethod(method): # ((RepRat, RepRat) -> T) -> ((RepOrd, RepRat) -> T)
        return lambda ord, rat: method(repord_to_reprat(ord), rat)


    def RRmethod_to_ROmethod(method): # ((RepRat, RepRat) -> T) -> ((RepRat, RepOrd) -> T)
        return lambda rat, ord: method(rat, repord_to_reprat(ord))

    ###########
    # Task 3a #
    ###########
    def add_ord_rat(x, y):
        return RRmethod_to_ORmethod(add_rat)(x, y)
    
    def sub_ord_rat(x, y):
        return RRmethod_to_ORmethod(sub_rat)(x, y)
    
    def mul_ord_rat(x, y):
        return RRmethod_to_ORmethod(mul_rat)(x, y)   

    def div_ord_rat(x, y):
        return RRmethod_to_ORmethod(div_rat)(x, y)
    
    def is_eq_ord_rat(x, y):
        return RRmethod_to_ORmethod(is_eq_rat)(x, y)
    
    put("add", ("ordinary", "rational"), add_ord_rat)
    put("sub", ("ordinary", "rational"), sub_ord_rat)
    put("mul", ("ordinary", "rational"), mul_ord_rat)
    put("div", ("ordinary", "rational"), div_ord_rat)
    put("is_equal", ("ordinary", "rational"), is_eq_ord_rat)

    def add_rat_ord(x, y):
        return RRmethod_to_ROmethod(add_rat)(x, y)
    
    def sub_rat_ord(x, y):
        return RRmethod_to_ROmethod(sub_rat)(x, y)
    
    def mul_rat_ord(x, y):
        return RRmethod_to_ROmethod(mul_rat)(x, y)
    
    def div_rat_ord(x, y):
        return RRmethod_to_ROmethod(div_rat)(x, y)
    
    def is_eq_rat_ord(x, y):
        return RRmethod_to_ROmethod(is_eq_rat)(x, y)
    
    put("add", ("rational", "ordinary"), add_rat_ord)
    put("sub", ("rational", "ordinary"), sub_rat_ord)
    put("mul", ("rational", "ordinary"), mul_rat_ord)
    put("div", ("rational", "ordinary"), div_rat_ord)
    put("is_equal", ("rational", "ordinary"), is_eq_rat_ord)



install_rational_package()

def create_rational(x,y):
    return get("make","rational")(x,y)

###########################
# Complex Number Package  #
###########################

# Copy and paste the install_complex_package procedure from Mission
# 11b below and complete the tasks below for this mission.

def install_complex_package():

    # Copy and paste your Mission 11b solution below here:
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

    ###########
    # Task 1b #
    ###########
    def repord_to_repcom(x): # RepOrd -> RepCom
        return repcom(create_ordinary(x), create_ordinary(0))

    ###########
    # Task 2b #
    ########### 
    def CCmethod_to_OCmethod(method): # ((RepCom, RepCom) -> T) -> ((RepOrd, RepCom) -> T)
        return lambda ord, com: method(repord_to_repcom(ord), com)


    def CCmethod_to_COmethod(method): # ((RepCom, RepCom) -> T) -> ((RepCom, RepOrd) -> T)
        return lambda com, ord: method(com, repord_to_repcom(ord))

    ###########
    # Task 3b #
    ###########
    def add_ord_com(x, y):
        return CCmethod_to_OCmethod(add_com)(x, y)
    
    def sub_ord_com(x, y):
        return CCmethod_to_OCmethod(sub_com)(x, y)
    
    def mul_ord_com(x, y):
        return CCmethod_to_OCmethod(mul_com)(x, y)
    
    def div_ord_com(x, y):
        return CCmethod_to_OCmethod(div_com)(x, y)
    
    def is_eq_ord_com(x, y):
        return CCmethod_to_OCmethod(is_eq_com)(x, y)
  
    put("add", ("ordinary", "complex"), add_ord_com)
    put("sub", ("ordinary", "complex"), sub_ord_com)
    put("mul", ("ordinary", "complex"), mul_ord_com)
    put("div", ("ordinary", "complex"), div_ord_com)
    put("is_equal", ("ordinary", "complex"), is_eq_ord_com)

    def add_com_ord(x, y):
        return CCmethod_to_COmethod(add_com)(x, y)
    
    def sub_com_ord(x, y):
        return CCmethod_to_COmethod(sub_com)(x, y)
    
    def mul_com_ord(x, y):
        return CCmethod_to_COmethod(mul_com)(x, y)
    
    def div_com_ord(x, y):
        return CCmethod_to_COmethod(div_com)(x, y)
    
    def is_eq_com_ord(x, y):
        return CCmethod_to_COmethod(is_eq_com)(x, y)
    
    put("add", ("complex", "ordinary"), add_com_ord)
    put("sub", ("complex", "ordinary"), sub_com_ord)
    put("mul", ("complex", "ordinary"), mul_com_ord)
    put("div", ("complex", "ordinary"), div_com_ord)
    put("is_equal", ("complex", "ordinary"), is_eq_com_ord)

install_complex_package()

def create_complex(x,y):
    return get("make","complex")(x,y)


#################
# Do not change #
#################

n3 = create_ordinary(3)
r3_1 = create_rational(create_ordinary(3), create_ordinary(1))
r2_7 = create_rational(create_ordinary(2), create_ordinary(7))

def gradeThis_rational_package():
    rationalA = is_equal(n3, r3_1)
    rationalB = is_equal(sub(add(n3, r2_7), r2_7), n3)
    if rationalA and rationalB:
        print("Well done! Your install_rational_package is complete!")
    else:
        print("Please check your solution for install_rational_package.")

n3 = create_ordinary(3)
c3_plus_0i = create_complex(create_ordinary(3), create_ordinary(0))
c2_plus_7i = create_complex(create_ordinary(2), create_ordinary(7))

def gradeThis_complex_package():
    complexA = is_equal(n3, c3_plus_0i)
    complexB = is_equal(sub(add(n3, c2_plus_7i), c2_plus_7i), n3)
    if complexA and complexB:
        print("Well done! Your install_complex_package is complete!")
    else:
        print("Please check your solution for install_complex_package.")

gradeThis_rational_package()
gradeThis_complex_package()

print(is_equal(r3_1, n3))
print(is_equal(n3, sub(add(n3, r2_7), r2_7)))
print()
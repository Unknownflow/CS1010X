def make_generator(op):
    def helper1(num1):
        def helper2(num2):
            return op(num2, num1)
        return helper2    
    return helper1

#################
# DO NOT REMOVE #
#################

def mul(x,y):
    return x*y

def pow(x,y):
    return x**y

make_multiplier = make_generator(mul)
make_exponentiator = make_generator(pow)

print(make_multiplier(3)(2))
print(make_exponentiator(3)(2))
def square(x):
    return x ** 2

# print(square(2))
print_square_2 = 4 # An example answer

# print(square(4)) 
print_square_4 = 16 # Insert your answer here


# print(square(square(square(2))))
print_square_square_square_2 = 256  # Insert your answer here


def f(x):
    return x * x

# print(f(4))
print_f_4 = 16 # Insert your answer here


def try_f(f):
    return f(3)

# print(try_f(f))
print_try_f_f = 9 # Insert your answer here

# print(try_f(f) == try_f(square))
print_try_try = True # Insert your answer here

# print(f(3) == square(3))
print_f_3_equals_square_3 = True # Insert your answer here

# print(f == square)
print_f_equals_square = False # Insert your answer here


def number_of_digits(x):
    # Fill in your code here
    digit_count = 1

    while x // 10 != 0:
        digit_count += 1
        x = x // 10

    return digit_count

print(number_of_digits(100))

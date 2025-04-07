# Practice Questions Set 1
# Q1a
def shift_one_left(num):
    num = str(num)
    num = num[1:] + num[0]
    return int(num)

# print(shift_one_left(12345))

# Q1b
def shift_left(num, n):
    if n == 0:
        return num
    else:
        num = shift_one_left(num)
        return shift_left(num, n-1)


#for i in range(8):
#    print(shift_left(12345, i))
#print()

# Q1c
def shift_left_alt(num, n):
    num = str(num)

    while n > 0:
        num = shift_one_left(num)
        n -= 1

    return num

#for i in range(8):
#    print(shift_left_alt(12345, i))

def shift_one_right(num):
    num = str(num)
    num = num[-1] + num[:-1]
    return int(num)

#print(shift_one_right(12345))
#print()

# Q1d
def shift_right(num, n):
    if n == 0:
        return num
    else:
        num = shift_one_right(num)
        return shift_right(num, n-1)

#print()
#print(shift_right(12345,1))
def shift_right_alt(num, n):
    num = str(num)

    while n > 0:
        num = shift_one_right(num)
        n -= 1

    return num

#for i in range(8):
#    print(shift_right(12345, i))
#print()


#for i in range(8):
#    print(shift_right_alt(12345, i))


# Q2
def nth_digit(n, num):
    if 10**n > num:
        return None
    if n == 1:
        remainder = num % 10
        print(n, num)
        return remainder
    else:
        num //= 10
        return nth_digit(n-1, num)

def nth_digit(n, num):
    if 10**n > num:
        return None
    for i in range(n-1):
        num = num // 10
        
    remainder = num % 10
    return remainder

print(nth_digit(1,12345))
print(nth_digit(3,12345))
print(nth_digit(4,12345))
print(nth_digit(10,12345))

def mth_digit(n, num):
    if n == 1:
        if len(str(num)) > 0:
            return int(str(num)[0])
        else:
            return None
    else:
        return mth_digit(n-1, str(num)[1:])

def mth_digit(n, num):
    if 10**n > num:
        return None
    res = None
    num = str(num)
    for i in range(n):
        res = num[i]

    return int(res)

print(mth_digit(1,12345))
print(mth_digit(3,12345))
print(mth_digit(4,12345))
print(mth_digit(10,12345))

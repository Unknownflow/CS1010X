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


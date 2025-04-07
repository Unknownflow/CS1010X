
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

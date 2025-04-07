def divisible_by_11(num):
    if num == 0:
        return True
    
    num = str(num)
    if len(num) == 1:
        return False
    else:
        sum_even = 0
        sum_odd = 0
        diff = 0

        for i in range(len(num)):
            digit = int(num[i])
            if i % 2 == 0:
                sum_even += digit
            else:
                sum_odd += digit

        if sum_even >= sum_odd:
            diff = sum_even - sum_odd
        else:
            diff = sum_odd - sum_even

        return divisible_by_11(diff)


def divisible_by_11(num):
    while num > 10:
        num = str(num)

        sum_even = 0
        sum_odd = 0

        for i in range(len(num)):
            digit = int(num[i])
            if i % 2 == 0:
                sum_even += digit
            else:
                sum_odd += digit

        if sum_even >= sum_odd:
            num = sum_even - sum_odd
        else:
            num = sum_odd - sum_even

    if num == 0:
        return True
    else:
        return False

for i in range(0, 250):
    print(i, divisible_by_11(i) == (i % 11 == 0))

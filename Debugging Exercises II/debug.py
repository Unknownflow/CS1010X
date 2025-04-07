def is_sum_odd(num):
    # Determine if the sum of digits is odd
    sum_digits = 0
    num = str(num)
    
    for i in range(len(num)):
        sum_digits += int(num[i])

    if sum_digits % 2 == 0:
        return False
    else:
        return True

print(is_sum_odd(12))
print(is_sum_odd(123789))
print(is_sum_odd(1))

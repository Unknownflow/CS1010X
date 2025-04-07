def concat(n, m):
    if n is None:
         return m
    else:
        length = len(str(m))
        n = str(n)

        if len(n) == 0:
            return concat(None, m)
        
        last_digit = int(n[-1])
        n = n[:-1]
        m = last_digit * (10 ** length) + m
        return concat(n, m)



def concat(n, m):
    length = len(str(m))
    while n > 0:
        remainder = n % 10
        n = n // 10
        m = remainder * (10 ** length) + m
        length += 1

    return m

print(concat(12345, 67890))
print(concat(1,0))
print(concat(11111,10000))

def cc(a, n):
    if a == 0:
        return 1
    elif a < 0:
        return 0
    elif n == 0:
        return 0
    else:
        return cc(a-denomination(n), n) + cc(a, n-1)

denom = (1,5,10,20,50)
def denomination(n):
    return denom[n-1]

print(cc(100,5))

def sum_tuple(t):
    if len(t) == 1:
        return t[0]
    else:
        return t[0] + sum_tuple(t[1:])


    
print(sum_tuple((3,4,5)))
print(sum_tuple((-1,-1,-2)))

def interleaved_tuple_adv(tuple_a, tuple_b):
    ptr = 0
    res = ()
    min_length = min(len(tuple_a), len(tuple_b))

    while ptr < min_length:
        res += (tuple_a[ptr], tuple_b[ptr])
        ptr += 1
    
    while ptr < len(tuple_a):
        res += (tuple_a[ptr], )
        ptr += 1
    
    while ptr < len(tuple_b):
        res += (tuple_b[ptr], )
        ptr += 1

    return res

print(interleaved_tuple_adv((1,3,5),(2,4,6,8,10,12)))
print(interleaved_tuple_adv((2,4,6,8,10,12),(1,3,5)))
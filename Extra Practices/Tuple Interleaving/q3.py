def interleaved_tuple_two(tuple_a, tuple_b):
    a_ptr = 0
    b_ptr = 0
    res = ()

    while a_ptr < len(tuple_a) and b_ptr < len(tuple_b):
        res += tuple_a[a_ptr:a_ptr+2] + (tuple_b[b_ptr],)
        a_ptr += 2
        b_ptr += 1
    
    while a_ptr < len(tuple_a):
        res += (tuple_a[a_ptr], )
        a_ptr += 1
    
    while b_ptr < len(tuple_b):
        res += (tuple_b[b_ptr], )
        b_ptr += 1

    return res

print(interleaved_tuple_two((1,3,5,7,9,11,13,15),(2,4,6,8)))
print(interleaved_tuple_two((2,4,6,8),(1,3)))
print(interleaved_tuple_two((1,1,1,1,1,1),(2,2,2)))
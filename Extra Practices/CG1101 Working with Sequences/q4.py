def reverse_tuple(tup):
    if len(tup) == 0:
        return tup

    return (tup[-1],) + reverse_tuple(tup[:-1])


print(reverse_tuple((-1, 1)))
print(reverse_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9)))
print(reverse_tuple((0,)))

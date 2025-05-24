def merge(tup1, tup2):
    res = ()
    ptr1 = 0
    ptr2 = 0
    len1 = len(tup1)
    len2 = len(tup2)

    while ptr1 < len1 and ptr2 < len2:
        if tup1[ptr1] < tup2[ptr2]:
            res += (tup1[ptr1],)
            ptr1 += 1
        else:
            res += (tup2[ptr2],)
            ptr2 += 1

    while ptr1 < len1:
        res += (tup1[ptr1],)
        ptr1 += 1

    while ptr2 < len2:
        res += (tup2[ptr2],)
        ptr2 += 1

    return res


print(merge((-3, 8, 65, 100, 207), (-10, 20, 30, 40, 65, 80, 90)))
print(merge((-1, 1, 3, 5, 7, 9, 11), (-2, 0, 3, 4, 6)))

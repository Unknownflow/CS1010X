def deep_reverse(lst):
    if type(lst) != list:
        return lst
    if len(lst) == 0:
        return lst
    return deep_reverse(lst[1:]) + [deep_reverse(lst[0])]


print(deep_reverse([1,2,[3,4],[[5]],[6,[7,8],9]]))
print(deep_reverse([1, [[[2, 3, 4, 5],6 ], 7], 8, [9, 10, [11]]]))
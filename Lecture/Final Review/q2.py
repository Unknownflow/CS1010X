def deep_sum(lst):
    if type(lst) != list:
        return lst
    if lst == []:
        return 0
    return deep_sum(lst[0]) + deep_sum(lst[1:])

print(deep_sum([1, [[[2, 3, 4, 5],6 ], 7], 8, [9, 10, [11]]]))
print(deep_sum([1, 2, [3, 4, [[5]], [[6], [7, 8], 9], 10]]))
print(deep_sum([1,2,3,4]))
print(deep_sum([]))
def power_set(input_list):
    # Start with the empty set
    result = [[]]

    for elem in input_list:
        for i in range(len(result)):
            new_list = result[i].copy()
            new_list.append(elem)
            result.append(new_list)

    return result


def power_set(a):
    if a == []:
        return [[]]
    else:
        result1 = power_set(a[1:])
        result2 = list(map(lambda x: x+[a[0]], result1))
        return result1 + result2


print(power_set([1, 2, 3]))
print(power_set([1, 2, 3, 4]))

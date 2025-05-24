def repeat(string):
    count = 0
    repeated = False

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            repeated = True
        else:
            if repeated:
                count += 1
            repeated = False

    if repeated:
        count += 1
    return count


print(repeat('mississippi'))
print(repeat('bbbb'))
print(repeat('hsSisSs'))
print(repeat('hssisss'))

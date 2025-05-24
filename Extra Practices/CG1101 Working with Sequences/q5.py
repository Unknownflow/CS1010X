def repeat(string):
    hashMap = {}
    for letter in string:
        if letter not in hashMap:
            hashMap[letter] = 1
        else:
            hashMap[letter] += 1

    res = 0
    for key, val in hashMap.items():
        if val > 1:
            res += 1

    return res


print(repeat('mississippi'))
print(repeat('abbA'))
print(repeat('hsSisSs'))
print(repeat('the QUICK bRoWn FoX'))

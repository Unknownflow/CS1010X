def split(n,lst):
    smaller_or_eq = []
    greater = []

    for num in lst:
        if num <= n:
            smaller_or_eq.append(num)
        else:
            greater.append(num)
            
    return [smaller_or_eq, greater]

print(split(5,[1,10,4,9,7,2,5,8,3,4,9,6,2]))
print(split(-4,[-10,0,-43,23,128312,-4,-4]))
print(split(20,[1,10,4,9,7,2,5,8,3,4,9,6,2]))
print(split(-20,[1,10,4,9,7,2,5,8,3,4,9,6,2]))


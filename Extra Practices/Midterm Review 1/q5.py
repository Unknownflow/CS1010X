def triangle_iterative(n):
    res = ""

    for i in range(1, n+1):
        res += i * "$" + "\n"
    
    return res

print(triangle_iterative(1))
print(triangle_iterative(4))
print(triangle_iterative(5))
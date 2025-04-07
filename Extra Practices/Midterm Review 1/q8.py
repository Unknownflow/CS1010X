def triangle_recursive(n):
    if n == 1:
        return "$\n"
    else:
        return triangle_recursive(n-1) + n * "$" + "\n"

print(triangle_recursive(1))
print(triangle_recursive(4))
print(triangle_recursive(5))

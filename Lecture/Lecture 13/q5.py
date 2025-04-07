
def num_of_paths(n, m):
    table = {}  # table to memoize computed values
    for i in range(n):
        for j in range(m):
            left = 0
            up = 0
            if (i-1, j) in table:
                left = table[(i-1, j)]
            
            if (i, j-1) in table:
                up = table[(i, j-1)]
            
            total = left + up

            if (i, j) not in table:
                if total == 0:
                    table[(i, j)] = 1
                else:
                    table[(i, j)] = left + up
            else:
                table[(i, j)] += left + up

    return table[(n-1, m-1)]
                

print(num_of_paths(1, 100))
print(num_of_paths(123, 1))
print(num_of_paths(3, 3))
print(num_of_paths(10, 10))
print(num_of_paths(28, 56))
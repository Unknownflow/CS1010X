def pascal(row, col):
    if col == 1 or col == row:
        return 1
    else:
        return pascal(row - 1, col) + pascal(row - 1, col - 1)

def faster_pascal(row, col):
    pascal_arr = [[1], [1, 1]]

    for i in range(2, row):
        new_row = [1]
        for j in range(i-1):
            new_row.append(pascal_arr[i-1][j] + pascal_arr[i-1][j+1])
        new_row.append(1)
        pascal_arr.append(new_row)

    return pascal_arr[row-1][col-1]

print(faster_pascal(3, 2))
print(faster_pascal(4, 3))
print(faster_pascal(100, 45))
print(faster_pascal(500, 3))
print(faster_pascal(1, 1))
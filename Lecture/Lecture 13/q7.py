def num_of_paths(maze):
    # Initialize an empty table (dictionary), get number of rows n and number of columns m
    table = {}
    n = len(maze)
    m = len(maze[0])

    # Fill in the first row. For j in range m: 
    # If maze[0][j] is safe, set table[(0, j)] to be 1 because there's one way to go there.
    # If maze[0][j] has a bomb, set table[(0, k)] where k >= j to be 0. Since one cell is broken along the way, all following cells cannot be reached.
    for j in range(m):
        if maze[0][j] == 1:
            table[(0, j)] = 1
        else:
            for k in range(j, m):
                table[(0, k)] = 0
            break

    # Fill in first column. For i in range n: 
    # If maze[i][0] is safe, set table[(i, 0)] to be 1 because there's one way to go there.
    # If maze[i][0] has a bomb, set table[(i, 0)] and all cells under it to be 0. The reason is same as row.
    for i in range(n):
        if maze[i][0] == 1:
            table[(i, 0)] = 1
        else:
            for k in range(i, n):
                table[(k, 0)] = 0
            break

    # Main DP procedure - fill in the rest of the table. If maze[i][j] has a bomb, set table[(i, j)] = 0. Otherwise, table[(i, j)] = table[(i - 1, j)] + table[(i, j - 1)] 
    for i in range(1, n):
        for j in range(1, m):
            if maze[i][j] == 0:
                table[(i, j)] = 0
            else:
                table[(i, j)] = table[(i-1, j)] + table[(i, j-1)]

    # Return table[(n - 1, m - 1)] 
    return table[(n-1, m-1)]
    

    
    
    
    
    
    
    
# Do NOT modify
maze1 = ((1, 1, 1, 1, 1, 1, 1, 1, 0, 1),
         (1, 0, 0, 1, 1, 1, 0, 0, 1, 1),
         (0, 1, 1, 1, 0, 0, 1, 1, 1, 0),
         (1, 1, 0, 1, 1, 1, 1, 0, 1, 1),
         (0, 1, 0, 1, 0, 0, 1, 0, 1, 0),
         (1, 0, 1, 1, 1, 1, 0, 1, 1, 1),
         (1, 1, 0, 1, 0, 1, 0, 0, 1, 1),
         (0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
         (1, 0, 1, 0, 0, 1, 1, 0, 1, 1),
         (1, 0, 1, 1, 1, 0, 1, 0, 1, 0),
         (1, 1, 0, 1, 0, 1, 0, 1, 1, 1))


maze2 = ((1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1))

maze3 = ((1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 0),
         (1, 0, 0, 1))

print(num_of_paths(maze1))
print(num_of_paths(maze2))
print(num_of_paths(maze3))
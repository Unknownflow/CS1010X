def binary_search(key, seq):  # seq is sorted.
    def helper(low, high):
        if low > high:
            return False
        mid = (low + high) // 2

        if key == seq[mid]:
            return True
        elif key < seq[mid]:
            return helper(low, mid-1)
        else:
            return helper(mid+1, high)
    return helper(0, len(seq)-1)

# Time: O(logn)
# Space: O(logn) recursive / O(1) if non recursive


a = [6, 2, 1, 7, 4, 5, 9]


def bubble_sort(lst):
    swaps = True

    while swaps:
        swaps = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                tmp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = tmp
                swaps = True

    return lst


def bubble_sort(arr):
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        # Initialize swapped to track if any swaps occur
        swapped = False
        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # Mark that a swap has occurred
                swapped = True

        # If no swaps occurred, the list is already sorted
        if not swapped:
            break

    return arr


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def selection_sort(array):
    for ind in range(len(array)):
        min_index = ind
        for j in range(ind + 1, len(array)):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        array[ind], array[min_index] = array[min_index], array[ind]

# Selection sort - find smallest / largest elem then swap
# Time - O(n^2) for all scenarios, space: O(1)


def merge_sort(lst):
    if len(lst) < 2:  # Base case!
        return lst
    left = merge_sort(lst[:len(lst)//2])
    right = merge_sort(lst[len(lst)//2:])
    return merge(left, right)


def merge(left, right):
    results = []
    while left and right:
        if left[0] < right[0]:
            results.append(left[0])
            left.remove(left[0])
        else:
            results.append(right[0])
            right.remove(right[0])
    results.extend(left)
    results.extend(right)
    return results

# Merge sort
# Time: O(nlogn) for all scenarios, space: O(n)


memoize_table = {}


def memoize(f, name):
    if name not in memoize_table:
        memoize_table[name] = {}
    table = memoize_table[name]

    def helper(*args):
        if args in table:
            return table[args]
        else:
            result = f(*args)
            table[args] = result
            return result
    return helper


def memo_fib(n):
    def helper(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return memo_fib(n-1) + memo_fib(n-2)
    return memoize(helper, "memo_fib")(n)


def dp_choose(n, k):
    row = [1]*(k+1)
    table = []
    for i in range(n+1):
        table.append(row.copy())

    for j in range(1, k+1):
        table[0][j] = 0

    for i in range(1, n+1):
        for j in range(1, k+1):
            table[i][j] = table[i-1][j-1] + table[i-1][j]
    return table[n][k]


def transpose(mat):
    transposed = [[0 for i in range(len(mat))] for j in range(len(mat[0]))]
    for col_idx in range(len(mat[0])):
        for row_idx in range(len(mat)):
            transposed[col_idx][row_idx] = mat[row_idx][col_idx]

    return transposed


def bfs(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        for i in node.children:
            queue.append(i)

# find shortest path
# count components in disconnected graph


def dfs(node):
    if not node:
        return
    else:
        for i in node.children:
            dfs(i)

# topological sort
# counting strongly connected components
# pre/in/post order traversal
# probs that require backtracking


def islands(map):
    DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def explore(row, col):
        queue = [(row, col)]
        while queue:
            x, y = queue.pop(0)
            if map[x][y] == "X":
                continue
            map[x][y] = "V"
            for d in DIRECTION:
                new_x = x + d[0]
                new_y = y + d[1]
                if 0 <= new_x < len(map) and 0 <= new_y < len(map[0]):
                    queue.append((new_x, new_y))
        return 1

    ans = 0
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == "X":
                explore(r, c)
                ans += 1

    return ans

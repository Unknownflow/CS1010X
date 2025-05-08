def binary_search(key, seq): #seq is sorted.
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


def selectionSort(array):
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
	return merge(left,right)
def merge(left,right):
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
        if  n==0:
            return 0
        elif n==1:
            return 1
        else:
            return memo_fib(n-1) + memo_fib(n-2)
    return memoize(helper, "memo_fib")(n)

def dp_choose(n,k):
    row = [1]*(k+1)
    table = []
    for i in range(n+1):
        table.append(row.copy())

    for j in range(1,k+1):
        table[0][j] = 0

    for i in range(1,n+1):
        for j in range(1,k+1):
            table[i][j] = table[i-1][j-1] + table[i-1][j]
    return table[n][k]

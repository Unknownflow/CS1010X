def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

print(bubble_sort([5,3,2,6,7,8,1,4]))
print(bubble_sort([3,4,5,-1,-7,0,3,4]))

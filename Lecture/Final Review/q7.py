def power_set_check(lst):
    longest_set = []
    for item in lst:
        if len(item) > len(longest_set):
            longest_set = item
    lst.sort()
    def power_set(input_list):
        # Start with the empty set
        result = [[]]
        
        # Iterate over every element in the input list
        for elem in input_list:
            # For each element, add it to all existing subsets in the result
            new_subsets = [subset + [elem] for subset in result]
            result.extend(new_subsets)

        result.sort()        
        return result
    
    return power_set(longest_set) == lst

print(power_set_check([[1,2,3],[1,2],[1,3],[2,3],[1],[2],[3],[]]))
print(power_set_check([[1, 2, 3]]))
print(power_set_check([[], ['lugia'], ['ho-oh'], ['ho-oh', 'lugia']]))
print(power_set_check([[], [2], [1, 2]]))
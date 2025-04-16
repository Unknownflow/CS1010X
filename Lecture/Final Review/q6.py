def power_set(input_list):
    # Start with the empty set
    result = [[]]
    
    # Iterate over every element in the input list
    for elem in input_list:
        # For each element, add it to all existing subsets in the result
        new_subsets = [subset + [elem] for subset in result]
        result.extend(new_subsets)
    
    return result

print(power_set([1,2,3]))
print(power_set([1,2,3,4]))
def normalize(lst):
    s = sum(lst)
    return list(map(lambda v: v / s, lst))

# print(normalize([1,2,5,4]))
# print(normalize([1,2,-7,4])) - division by 0 error where sum is 0

def safe_normalize(lst):
    try:
        # Try normalizing the list using the already defined normalize function
        return normalize(lst)
    except ZeroDivisionError:
        # If a ZeroDivisionError occurs, return the list unchanged
        return lst

print(safe_normalize([1,2,5,4]))
print(safe_normalize([1,2,-7,4]))

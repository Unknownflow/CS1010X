def max_and_min(t):
    """Returns a tuple containing the max and min value in tuple t"""
    def max(t):
        if len(t) == 1:
            return t
        else:
            if t[0] < t[1]:
                return max(t[1:])
            else:
                return max((t[0],) + t[2:])

    def min(t):
        if len(t) == 1:
            return t
        else:
            if t[0] > t[1]:
                return min(t[1:])
            else:
                return min((t[0],) + t[2:])
            
    return max(t) + min(t)

print(max_and_min((2,10,9,3,4)))
print(max_and_min((1,-9,-2,29,3)))

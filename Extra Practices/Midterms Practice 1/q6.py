def replace_digit(n, d, r):
    # to replace d with r in n
    res = ""
    n = str(n)

    for i in range(len(n)):
        if int(n[i]) == d:
            res += str(r)
        else:
            res += n[i]
            
    return int(res)


def replace_digit(n, d, r):
    # to replace d with r in n
    def helper(n, d, r):
        if n == "":
            return n
        else:
            if len(str(n)) == 0:
                return ""
            n = str(n)
            first_digit = n[0]
            #print(n[0])
            if int(n[0]) == d:
                n = (n[1:])

                return (str(r) + helper(n, d, r))
            else:
                n = (n[1:])

                return (first_digit + helper(n, d, r))
    return int(helper(n, d, r))

print(replace_digit(31242154125, 1, 0))

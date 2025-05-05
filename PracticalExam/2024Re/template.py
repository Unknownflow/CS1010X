# A stack class which you can use when you implement your functions.
# If you use this class in your solutions, please copy and paste the code to Coursemology as well.
class stack(object):
    def __init__(self):
        self.lst = []
    def push(self, x): # push an element to the stack
        self.lst.append(x)
    def pop(self): # pop the top element in the stack
        return self.lst.pop(-1)
    def top(self): # get the top element in the stack
        return self.lst[-1]
    def size(self): # get the size of the stack
        return len(self.lst)
    def empty(self): # return True if the stack is empty, otherwise False
        return self.size() == 0


# Q1
def generate_key(s):
    alphabets = {}
    res = ""
    a_ord_val = ord("a")

    for i in range(a_ord_val, a_ord_val + 26):
        alphabets[chr(i)] = 0
    
    for letter in s:
        if letter == " ":
            continue
        else:
            alphabets[letter] += 1

    alphabets_lst = [(key, val) for key, val in alphabets.items()]
    for i in range(len(alphabets_lst)):
        for j in range(len(alphabets_lst)-1):
            if alphabets_lst[j][1] < alphabets_lst[j+1][1]:
                alphabets_lst[j], alphabets_lst[j+1] = alphabets_lst[j+1], alphabets_lst[j]
            elif alphabets_lst[j][1] == alphabets_lst[j+1][1]:
                if alphabets_lst[j][0] > alphabets_lst[j+1][0]:
                    alphabets_lst[j], alphabets_lst[j+1] = alphabets_lst[j+1], alphabets_lst[j]

    for alphabet in alphabets_lst:
        res += alphabet[0]
    return res

print('=' * 9, 'Question 1', '=' * 9)
print(generate_key("the lazy fox jumps over a brown dog"))
print("oaerbdfghjlmnpstuvwxyzcikq")


# Q2
def encrypt(msg, s):
    key = generate_key(s)
    res = ""
    a_ord_val = ord("a")
    for char in msg:
        if char.isalpha() and char.islower():
            char_ord_val = ord(char)
            diff = char_ord_val - a_ord_val
            res += key[diff]
        else:
            res += char
    return res

print('=' * 9, 'Question 2', '=' * 9)
print(encrypt("##Hello World!!", "the lazy fox jumps over a brown dog"))


# Q3
def decrypt(msg, s):
    key = generate_key(s)
    res = ""
    a_ord_val = ord("a")
    for char in msg:
        if char.isalpha() and char.islower():
            idx = key.index(char)
            res += chr(a_ord_val + idx)
        else:
            res += char
    return res

print('=' * 9, 'Question 3', '=' * 9)
print(decrypt("##Hbmms Wsvmr!!", "the lazy fox jumps over a brown dog"))


# Q4
def leader(A):
    res = []

    for i in range(len(A)):
        found = False
        for j in range(i, len(A)):
            if A[j] > A[i]:
                res.append(A[j])
                found = True
                break
        
        if not found:
            res.append(A[i])
    return res
    

print('=' * 9, 'Question 4', '=' * 9)
print(leader([1, 2, 1, 3, 2, 4, 5, 7, 6]))


# Q5
def k_leader(A, k):
    res = []

    for i in range(len(A)):
        found = False
        for j in range(i+k, len(A)):
            if A[j] > A[i]:
                res.append(A[j])
                found = True
                break
        
        if not found:
            res.append(A[i])
    return res

print('=' * 9, 'Question 5', '=' * 9)
print(k_leader([1, 2, 1, 3, 2, 4, 5, 7, 6], 2))


# Q6
def minimum(A):
    res = 10000000000000000000000000000000000000000000000000000000
    if len(A) == 1:
        return A[0]
    
    for x in range(A[0], A[-1]+1):
        total = 0
        for num in A:
            total += abs(num - x)
        if total < res:
            res = total
        else:
            return total

print('=' * 9, 'Question 6', '=' * 9)
print(minimum([1, 2, 3, 5, 6, 7]))
print(minimum([1, 3, 7, 8, 11, 17, 25, 31]))


# Q7
def constrained_minimum(A, k):
    def minimum(A):
        res = 10000000000000000000000000000000000000000000000000000000
        if len(A) == 1:
            return (A[0], 0)
        for x in range(A[0], A[-1]+1):
            total = 0
            for num in A:
                total += abs(num - x)
            if total < res:
                res = total
            else:
                return (x, total)
    first_min = minimum(A[0])
    second_min = minimum(A[1])
    third_min = minimum(A[2])
    print('s',first_min, second_min, third_min)
    if first_min[0] - second_min[0] >= k and second_min[0] - third_min[0] >= k:
        return first_min[1] + second_min[1] + third_min[1]
    else:
        return 'wtf'
    

print('=' * 9, 'Question 7', '=' * 9)
print(constrained_minimum([[1, 2, 3, 5, 6, 7], [2, 2, 3, 3, 6, 7], [1, 1, 3, 5, 5]], 2))
print(constrained_minimum([[4], [5], [6]], 10))


# Q8
def constrained_minimum_adv(A, k):
    pass

print('=' * 9, 'Question 8', '=' * 9)
print(constrained_minimum_adv([[1, 2, 3, 5, 6, 7], [2, 2, 3, 3, 6, 7], [1, 1, 3, 5, 5], [1, 2, 5, 8, 9]], 2))
print(constrained_minimum_adv([[4], [5], [6], [7]], 10))

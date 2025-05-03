# Question 1
def dec_to_base(dec, base):
    res = 0
    pow = 0
    while dec > 0:
        res += (dec % base) * 10 ** pow
        dec //= base
        pow += 1
    return res

print('=' * 9, 'Question 1', '=' * 9)
print(dec_to_base(123, 5))
print(dec_to_base(443, 9))


# Question 2
def encode(S, base_lst):
    res = ""
    pos = 0
    for char in S:
        base = base_lst[pos]
        res += "#" + str(base) + "#" + str(dec_to_base(ord(char), base)) 
        pos = (pos + 1) % len(base_lst)
    return res

print('=' * 9, 'Question 2', '=' * 9)
print(encode('hello', [5, 3, 7]))
print(encode('world', [4, 6, 8]))


# Question 3
def base_to_dec(num, base):
    res = 0
    pow = 0
    while num > 0:
        remainder = num % 10
        res += remainder * (base ** pow)
        pow += 1
        num //= 10
    
    return res

print('=' * 9, 'Question 3', '=' * 9)
print(base_to_dec(11010, 3))


# Question 4
def decode(S):
    S_items = S[1:].split("#")
    res = ""
    for i in range(0, len(S_items), 2):
        base = int(S_items[i])
        ascii_code = int(S_items[i+1])
        ord_num = base_to_dec(ascii_code, base)
        res += chr(ord_num)
    return res

print('=' * 9, 'Question 4', '=' * 9)
print(decode('#5#404#3#10202#7#213#5#413#3#11010'))


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


# Question 5
def arrange(car_lst, commands):
    stack = []
    queue = []
    car_count = 0
    for i in range(len(commands)):
        if car_count > len(car_lst) - 1:
            car_count = len(car_lst) - 1
        car = car_lst[car_count]
        command = commands[i]
        if command == "Q":
            queue = [car] + queue
            car_count += 1
        elif command == "P":
            stack.append(car)
            car_count += 1
        elif command == "PQ":
            popped = stack.pop()
            queue = [popped] + queue
    
    while len(stack) > 0:
        popped = stack.pop()
        queue.append(popped)
    
    return queue

print('=' * 9, 'Question 5', '=' * 9)
print(arrange([1, 4, 7, 9, 11, 15], ['P', 'Q', 'PQ', 'Q', 'P', 'P', 'Q', 'PQ', 'PQ']))


# Question 6
def check(car_lst_in, car_lst_out):
    car_out_idx = len(car_lst_out) - 1
    car_in_idx = 0
    queue = []
    stack = []

    while car_out_idx >= 0:
        next = car_lst_out[car_out_idx]

        if next in stack:
            while True:
                popped = stack.pop()
                queue = [popped] + queue
                if popped == next:
                    break
        else:
            found = False

            while car_in_idx < len(car_lst_in) and not found:
                car = car_lst_in[car_in_idx]
                if car == next:
                    found = True
                    queue = [car] + queue
                else:
                    stack.append(car)
                car_in_idx += 1
        car_out_idx -= 1
    

    if queue == car_lst_out:
        return "possible"
    else:
        return "impossible"

print('=' * 9, 'Question 6', '=' * 9)
print(check([1, 4, 7, 23, 45, 67], [67, 45, 23, 7, 4, 1]))
print(check([1, 2, 4, 6, 7, 9, 11, 15, 16], [4, 6, 16, 7, 15, 9, 11, 2, 1]))
print(check([1, 2, 4, 6, 7, 9, 11, 15, 16], [4, 7, 16, 6, 15, 9, 11, 2, 1]))


# Question 7
def ACB(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                if lst[i] < lst[k] < lst[j]:
                    return True
    return False

print('=' * 9, 'Question 7', '=' * 9)
print(ACB([1, 2, 3, 4, 5, 6, 7, 8]))
print(ACB([1, 2, 3, 4, 7, 8, 9 ,5]))
print(ACB([8, 7, 6, 5, 4, 3, 2, 1]))


# Question 8
def ACB(lst):
    less_than_count = 0
    more_than_count = 0
    less_than_idx = []
    more_than_idx = []
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            less_than_count += 1
            less_than_idx.append(i)
        elif lst[i] > lst[i+1]:
            more_than_count += 1
            more_than_idx.append(i)
    
    if less_than_count == 0 or more_than_count == 0:
        return False
    else:
        if less_than_idx[0] < more_than_idx[-1]:
            return True            
        return False
        

print('=' * 9, 'Question 8', '=' * 9)
print(ACB([1, 2, 3, 4, 5, 6, 7, 8]))
print(ACB([1, 2, 3, 4, 7, 8, 9 ,5]))
print(ACB([8, 7, 6, 5, 4, 3, 2, 1]))
print(ACB([1,1,1,1,1,2]))

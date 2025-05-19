# Q1
import random
plain = [['0', '1', '2', '3', '4', '5'],
         ['6', '7', '8', '9', 'A', 'B'],
         ['C', 'D', 'E', 'F', 'G', 'H'],
         ['I', 'J', 'K', 'L', 'M', 'N'],
         ['O', 'P', 'Q', 'R', 'S', 'T'],
         ['U', 'V', 'W', 'X', 'Y', 'Z']]

message = "HELLO 1 2 3"


def encrypt(message, plain, c1, c2):  # '012345', 'ABCDEF'):
    res = ""
    for char in message:
        if char == " ":
            res += char
        else:
            for i in range(len(plain)):
                for j in range(len(plain[0])):
                    if plain[i][j] == char:
                        res += c1[i]
                        res += c2[j]
                        break

    return res


secret = encrypt(message, plain, '062849', 'abcdef')
# print(secret)

# Q2


def decrypt(secret, plain, c1, c2):
    res = ""
    curr_ptr = 0
    length = len(secret)
    while curr_ptr < length:
        if secret[curr_ptr] == " ":
            res += " "
            curr_ptr += 1
        else:
            row_idx = c1.index(secret[curr_ptr])
            col_idx = c2.index(secret[curr_ptr + 1])
            res += plain[row_idx][col_idx]
            curr_ptr += 2

    return res

# print( decrypt(secret, plain, '062849', 'abcdef'))

# Q3


def index(lst, char):
    def helper(lst, char, output, curr_idx):
        if len(lst) == 0:
            return None
        if char in lst:
            if output == "":
                return str(lst.index(char))
            if output != "" and output[-1] == "-":
                return output + str(lst.index(char))
            else:
                startFrom = 0
                output = output + "-" + str(lst.index(char))
                for i in range(len(output)-1):
                    if output[i] == "-" and output[i+1] == "-":
                        startFrom = i+1

                return output[startFrom+1:]
        if type(lst[0]) == list:
            if output == "":
                output = str(curr_idx) + "-"
            else:
                output = output + "-" + str(curr_idx)
            return helper(lst[0], char, output, 0) or helper(lst[1:], char, output, curr_idx+1)
        else:
            return helper(lst[1:], char, output, curr_idx+1)

    return helper(lst, char, "", 0)


def index(lst, char):
    res = []
    flag = False

    def helper(currlst):
        nonlocal flag
        if type(currlst) != list:
            if currlst == char:
                flag = True
            return
        for i in range(len(currlst)):
            res.append(i)
            helper(currlst[i])
            if flag:
                return
            res.pop()

    helper(lst)
    if not res:
        return None
    res_string = ""
    for num in res:
        res_string += str(num) + "-"

    return res_string[:-1]


lst = [0, [1, 2, 3, 4], [5, 6, [7, [8, 9, [10, [11, [12]]]]]]]
for i in range(13):
    print("index of", i, "in", lst, "is:", index(lst, i))

# Q4 - you are not allowed to use any library functions


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


def make_rotation_matrix(m, n):
    matrix = []
    row = [i for i in range(0, n)]
    for i in range(m):
        matrix.append(row)
        row = list(row)
        popped = row.pop(0)
        row.append(popped)

    return matrix

# print("rotating")
# print_matrix(make_rotation_matrix(5, 5))
# print()
# print_matrix(make_rotation_matrix(6, 5))

# Q5


def make_symmetrical_matrix(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        matrix[0][i] = i
        matrix[i][0] = i

    for i in range(1, n):
        for j in range(1, n):
            matrix[i][j] = matrix[i-1][j-1]
    return matrix


print("symmetric")
# print_matrix(make_symmetrical_matrix(6))

# Q6


def make_concentric_matrix(m, n):
    matrix = [[0 for i in range(n)] for j in range(m)]
    curr_num = 1
    left_ptr = 1
    top_ptr = 1
    right_ptr = n-2
    bottom_ptr = m-2
    while left_ptr <= right_ptr and top_ptr <= bottom_ptr:
        for i in range(left_ptr, right_ptr + 1):
            matrix[top_ptr][i] = curr_num
            matrix[bottom_ptr][i] = curr_num

        for i in range(top_ptr, bottom_ptr + 1):
            matrix[i][left_ptr] = curr_num
            matrix[i][right_ptr] = curr_num

        curr_num += 1
        left_ptr += 1
        right_ptr -= 1
        top_ptr += 1
        bottom_ptr -= 1

    return matrix


print("concentric")
# print_matrix(make_concentric_matrix(3,3))
# print_matrix(make_concentric_matrix(4,4))
# print_matrix(make_concentric_matrix(5,5))
# print_matrix(make_concentric_matrix(5,6))

# print_matrix(make_concentric_matrix(5,10))

# Q7


def make_diamond_matrix(m, n):
    matrix = [[0 for i in range(n)] for j in range(m)]
    if m % 2 == 0:
        if n % 2 == 0:
            for i in range(m // 2):
                for j in range(n // 2):
                    matrix[i][j] = j + i
                    matrix[i][n-j-1] = j + i

        else:
            for i in range(m // 2):
                for j in range(n // 2 + 1):
                    matrix[i][j] = j + i
                    matrix[i][n-j-1] = j + i
        diff = 1
        for i in range(m // 2, m):
            for j in range(n):
                matrix[i][j] = matrix[i-diff][j]
            diff += 2
    else:
        if n % 2 == 0:
            for i in range(m // 2 + 1):
                for j in range(n // 2):
                    matrix[i][j] = j + i
                    matrix[i][n-j-1] = j + i

        else:
            for i in range(m // 2 + 1):
                for j in range(n // 2 + 1):
                    matrix[i][j] = j + i
                    matrix[i][n-j-1] = j + i

        diff = 2
        for i in range(m // 2 + 1, m):
            for j in range(n):
                matrix[i][j] = matrix[i-diff][j]
            diff += 2

    return matrix


print("diamond")
print_matrix(make_diamond_matrix(7, 7))
print()
# print_matrix(make_diamond_matrix(8,8))
print()
print_matrix(make_diamond_matrix(7, 8))
print()
# print_matrix(make_diamond_matrix(8,7))

# Q8 - Q10


class Node(object):
    def __init__(self, num, before, after, top, bottom):
        self.num = num
        self.before = before    # node before the current node
        self.after = after      # node after the current node
        self.top = top          # its copy above the current layer
        self.bottom = bottom    # a copy below the current layer


def insert_into(head, num):
    if head == None:
        # this is the very first node in the list
        return Node(num, None, None, None, None)

    previous = None
    current = head
    while current != None:
        if num < current.num:
            # insert newNode before the current node
            newNode = Node(num, previous, current, None, None)
            if previous != None:
                previous.after = newNode
            if current.before == None:
                head = newNode
            current.before = newNode
            return head
        previous = current
        current = current.after
    # insert newNode after the last node in the current list
    newNode = Node(num, previous, None, None, None)
    previous.after = newNode
    return head

# Q8


def all_keys(node):
    curr = node
    res = ""

    while curr != None:
        res += str(curr.num) + "-"
        curr = curr.after

    if len(res) > 0 and res[-1] == "-":
        return res[:-1]
    else:
        return res


lst = None
for i in [4, 3, 16, 14, 24, 2, 5, 22, 17, 9, 1, 6, 11, 7, 18, 12, 13]:
    lst = insert_into(lst, i)

# Q9


def search_layer(node, num):
    curr = node
    res = ""
    found = False

    while curr != None and not found:
        if curr.num >= num:
            found = True
        res += str(curr.num) + "-"
        curr = curr.after

    if len(res) > 0 and res[-1] == "-":
        return res[:-1]
    else:
        return res

# print("Current full list is:", all_keys(lst))
# for i in range(1,27,5):
    # print("visited nodes in searching for", i, ":", search_layer(lst, i))


# Q10
random.seed(1)          # let's use this seed for our testing
# input is a non-empty lst with the first element always smallest


def create_top(lst):
    topLst = Node(lst.num, None, None, None, lst)
    previous = topLst
    current = lst.after
    while current != None:
        rand = random.randint(0, 10)
        if rand <= 3:
            newNode = Node(current.num, previous, None, None, current)
            previous.after = newNode
            current.top = newNode
            previous = newNode
        current = current.after
    return topLst


topLst = create_top(lst)
print("Current topLst:", all_keys(topLst))

topMostLst = create_top(topLst)

print("Current topMostLst:", all_keys(topMostLst))


def search(topMostLst, num):
    curr = topMostLst
    found = False
    res = ""

    while curr != None and not found:
        if curr.num == num:
            found = True
            res += str(curr.num)
            break
        elif curr.num > num:
            res += str(curr.num) + "-"
            if curr:
                curr = curr.before
                if curr:
                    curr = curr.bottom
                    if curr:
                        curr = curr.after
                else:
                    break
            continue

        res += str(curr.num) + "-"
        if curr.after:
            if curr.after.num > num:
                curr = curr.bottom
                if curr:
                    curr = curr.after
            else:
                curr = curr.after
        else:
            curr = curr.bottom
            if curr:
                curr = curr.after

    if len(res) > 0 and res[-1] == "-":
        return res[:-1]
    else:
        return res


def search(topMostList, num):
    curr = topMostList
    res = ""

    while curr:
        if curr.num >= num:
            res += str(curr.num) + "-"
            break
        else:
            if curr.after:
                if curr.after.num <= num:
                    res += str(curr.num) + "-"
                    curr = curr.after
                else:
                    if curr.bottom:
                        curr = curr.bottom
                    else:
                        res += str(curr.num) + "-"
                        curr = curr.after
            else:
                if curr.bottom:
                    curr = curr.bottom
                else:
                    res += str(curr.num) + "-"
                    curr = curr.after

    return res[:-1]


for i in range(25):
    print("searching using 1 list", i, ":", search(lst, i))

print()
for i in range(26):
    print("searching using 2 lists", i, ":", search(topLst, i))

print()
for i in range(26):
    print("searching using 3 lists", i, ":", search(topMostLst, i))

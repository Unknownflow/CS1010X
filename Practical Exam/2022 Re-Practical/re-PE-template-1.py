# Q1
plain = [ ['0','1','2','3','4','5'],
           ['6','7','8','9','A','B'],
           ['C','D','E','F','G','H'],
           ['I','J','K','L','M','N'],
           ['O','P','Q','R','S','T'],
           ['U','V','W','X','Y','Z'] ]

message = "HELLO 1 2 3"
def encrypt(message, plain, c1, c2): #'012345', 'ABCDEF'):
    pass

secret = encrypt(message, plain, '062849', 'abcdef')
print(secret)

# Q2
def decrypt(secret, plain, c1, c2):
    pass

print( decrypt(secret, plain, '062849', 'abcdef'))

# Q3
def index(lst, char):
    pass

lst = [0,[1,2,3,4],[5,6,[7,[8,9]]]]
for i in range(12):
    print("index of", i, "in", lst, "is:", index(lst, i))

# Q4 - you are not allowed to use any library functions
def print_matrix(matrix):
    for i in range(len(matrix)):
        print (matrix[i])
        
def make_rotation_matrix(m, n):
    pass

print("rotating")
#print_matrix(make_rotation_matrix(5, 5))

# Q5
def make_symmetrical_matrix(n):
    pass

print("symmetric")
#print_matrix(make_symmetrical_matrix(6))

# Q6
def make_concentric_matrix(m,n):
    pass

print("concentric")
#print_matrix(make_concentric_matrix(5,10))

# Q7
def make_diamond_matrix(m,n):
    pass

print("diamond")
#print_matrix(make_diamond_matrix(7,7))


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
            newNode = Node(num, previous , current, None, None)
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
    pass

lst = None
for i in [4,3,16,14,24,2,5,22,17,9,1,6,11,7,18,12,13]:
    lst = insert_into(lst, i)

# Q9
def search_layer(node, num):
    pass

print("Current full list is:", all_keys(lst))
for i in range(1,26,5):
    print("visited nodes in searching for", i, ":", search_layer(lst, i))

# Q10
import random
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
    pass

for i in range(25):
    print("searching using 1 list", i, ":", search(lst, i))    

for i in range(25):
    print("searching using 2 lists", i, ":", search(topLst, i))    

for i in range(25):
   print("searching using 3 lists", i, ":", search(topMostLst, i))






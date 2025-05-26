#----------------
#    TOPIC 1
#----------------

# Question 1

def record(f):
    """Please do not paste the record function to Coursemology"""
    def helper(*args):
        global count
        count += 1
        return f(*args)
    return helper

@record # include this line in your submission
def jump_locate(aList, begin, end, jump, num_to_find):
    pass

# count = 0
# print(jump_locate(list(range(1, 10000, 2)), 0, 4999, 1, 1001))
# print(count)

# count = 0
# print(jump_locate(list(range(1, 10000, 2)), 0, 4999, 1, 1000))
# print(count)


#----------------
#    TOPIC 2
#----------------

def print_tree(tree):
    """Function to print a binary tree in friendly format. Do not modify and do not submit to Coursemology."""
    def to_str(tree):
        if tree == ():
            return [], 0, 0
        if tree[1] == () and tree[2] == ():
            _lst = [f'({tree[0]:03d})']
            return _lst, 5, 2
        ltree, lwidth, lpos = to_str(tree[1])
        rtree, rwidth, rpos = to_str(tree[2])
        _lst = [' ' * lwidth + f'({tree[0]:03d})' + ' ' * rwidth]
        line = (' ' * lpos + '+' + '-' * (lwidth - lpos + 1) + '+' if lwidth else '  +') \
            + ('-' * (rpos + 2) + '+' + ' ' * (rwidth - rpos - 1) if rwidth else '  ')
        _lst.append(line)
        for i in range(max(len(ltree), len(rtree))):
            line = (ltree[i] if i < len(ltree) else ' ' * lwidth) + ' ' * 5 \
                + (rtree[i] if i < len(rtree) else ' ' * rwidth)
            _lst.append(line)
        return _lst, len(_lst[0]), lwidth + 2
    try:
        lst = to_str(tree)[0]
        for s in lst:
            print(s)
    except:
        print('Something went wrong. Your input might be invalid.')

# iTupleList is just a list of public test cases for your convenience
iTupleList = []
iTupleList.append(((8, -1, 6), (7, 4, 9), (5, 1, 2), (1, 7, -1), (2, 3, 8), (3, -1, 0)))
iTupleList.append(((0, 1, 2),))
iTupleList.append(((0, 2, -1), (1, 0, -1)))
iTupleList.append(((2, -1, 0), (0, -1, 1)))
iTupleList.append(((0, 3, 2), (1, 4, 0)))

# Question 2

def find_root(iTuple):
    pass

# for iTuple in iTupleList:
#     print(find_root(iTuple))

# Question 3

def binary_tree(iTuple):
    pass

# for iTuple in iTupleList:
#     tree = binary_tree(iTuple) 
#     print(tree)
#     print_tree(tree)


#----------------
#    TOPIC 3
#----------------

# Question 4

class Tribes():
    def __init__(self, N):
        # Use a dictionary to capture the leader for each of the N tribes
        pass

    def tribe_leader(self, A):
        # Find the leader of tribe A, which is A if no one has conquered it before,
        # or ... (this is related to what you do for the next function, conquer)
        pass

    def conquer(self, A, B):
        # Purpose: Tribe A conquers tribe B
        pass

    def is_same_tribe(self, A, B):
        # Return True if tribe A and tribe B have the same leader,
        # otherwise return False
        pass

# def testTribes():
#     N = 100
#     T = Tribes(N)
#     T.conquer(10, 20)
#     print(T.tribe_leader(20))
#     print(T.is_same_tribe(20, 11))
#     T.conquer(5, 10)
#     T.conquer(10, 11)
#     print(T.is_same_tribe(20, 11))

# testTribes()


#----------------
#    TOPIC 4
#----------------

# Question 5

def subtree_distance(tree):
    dist = [0 for i in range(len(tree))]
    
    for i in range(len(tree)):
        child = i
        parent = tree[i]
        while parent != -1:
            dist[parent] = max(dist[parent], dist[child] + 1)
            child = parent
            parent = tree[parent]

    return dist

print(subtree_distance([-1, 0, 0, 1, 2, 2, 5]))
print(subtree_distance([-1, 0, 0, 1, 2, 2, 5, 6, 7]))



# Question 6

def tree_distance(tree):
    subtree_dist = subtree_distance(tree)
    
    pass

# print(tree_distance([-1, 0, 0, 1, 2, 2, 5]))
# print(tree_distance([-1, 0, 0, 1, 2, 3, 4]))


#----------------
#    TOPIC 5
#----------------

# Question 7
def count_bugles(n, m):
    pass

# print(count_bugles(3, 3))
# print(count_bugles(4, 5))

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
    if begin > end:
        return "Not Found"
    if begin + jump > end:
        jump = end - begin

    if aList[begin] == num_to_find:
        return begin
    else:
        if aList[begin+jump] == num_to_find:
            return begin + jump
        elif aList[begin+jump] < num_to_find:
            return jump_locate(aList, begin+jump+1, end, jump*2, num_to_find)
        else:
            return jump_locate(aList, begin+1, begin+jump-1, 1, num_to_find)

##count = 0
##print(jump_locate(list(range(1, 10000, 2)), 0, 4999, 1, 1001))
##print(count)
##
##count = 0
##print(jump_locate(list(range(1, 10000, 2)), 0, 4999, 1, 1000))
##print(count)


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
    nodes = []
    root = None
    
    for node in iTuple:
        val, left, right = node
        if val not in nodes:
            root = val
            nodes.append(val)
            
        if left != -1 and left not in nodes:
            nodes.append(left)
        if right != -1 and right not in nodes:
            nodes.append(right)

    return root

#for iTuple in iTupleList:
#    print(find_root(iTuple))

# Question 3

def binary_tree(iTuple):
    root = find_root(iTuple)
    
    def helper(root):
        if root == -1:
            return ()
        
        for node in iTuple:
            val, left, right = node
            if val == root:
                return (root, helper(left), helper(right))

        return (root, (), ())
    return helper(root)

##for iTuple in iTupleList:
##    tree = binary_tree(iTuple)
##    print()
##    print(tree)
##    print_tree(tree)


#----------------
#    TOPIC 3
#----------------

# Question 4

class Tribes():
    def __init__(self, N):
        # Use a dictionary to capture the leader for each of the N tribes
        self.N = N
        self.leaders = {}
        for i in range(1, N+1):
            self.leaders[i] = i

    def tribe_leader(self, A):
        # Find the leader of tribe A, which is A if no one has conquered it before,
        # or ... (this is related to what you do for the next function, conquer)
        if self.leaders[A] == A:
            return A
        else:
            return self.tribe_leader(self.leaders[A])

    def conquer(self, A, B):
        # Purpose: Tribe A conquers tribe B
        self.leaders[B] = A

    def is_same_tribe(self, A, B):
        # Return True if tribe A and tribe B have the same leader,
        # otherwise return False
        return self.tribe_leader(A) == self.tribe_leader(B)

##def testTribes():
##    N = 100
##    T = Tribes(N)
##    T.conquer(10, 20)
##    print(T.tribe_leader(20))
##    print(T.is_same_tribe(20, 11))
##    T.conquer(5, 10)
##    T.conquer(10, 11)
##    print(T.is_same_tribe(20, 11))
##
##testTribes()


#----------------
#    TOPIC 4
#----------------

# Question 5

def subtree_distance(tree):
    dist = [0 for i in range(len(tree))]
    dist[0] = 1
    for i in range(len(tree)-1, 0, -1):
        dist[tree[i]] += 1

    return dist

#print(subtree_distance([-1, 0, 0, 1, 2, 2, 5]))

# Question 6

def tree_distance(tree):
    dist = subtree_distance(tree)
    nodes = {}
    for i in range(1, len(tree)):
        if tree[i] not in nodes:
            nodes[tree[i]] = [i]
        else:
            nodes[tree[i]].append(i)
    sorted(nodes)

    for root, child in nodes.items():
        if len(child) == 1:
            dist[child[0]] = dist[root] + 1
        else:
            left, right = child
            if dist[left] == dist[right]:
                dist[left] = max(dist[root] + 1, dist[left])
                dist[right] = max(dist[root] + 1, dist[right])
            elif dist[left] < dist[right]:
                dist[left] = max(dist[root] + 1, dist[left], dist[right] + 2)
                dist[right] = max(dist[right], dist[root] )
            else:
                dist[left] = max(dist[root] + 1, dist[left])
                dist[right] = max(dist[root] + 1, dist[right], dist[left] + 2)

    return dist

#print(tree_distance([-1, 0, 0, 1, 2, 2, 5]))
#print(tree_distance([-1, 0, 0, 1, 2, 3, 4]))


#----------------
#    TOPIC 5
#----------------

# Question 7
def count_bugles(n, m):
    if n == 1 or m == 1:
        return 0
    count = 0
    small_triangle = (n-1) * (m-1) * 4
    count += small_triangle
    print(count)
    for i in range(2,n):
        num_i = n // i
        num_j = m // i
        count += 12 * num_i * num_j
        print(count)

    return count

#print(count_bugles(3, 3))
#print(count_bugles(3, 4))
#print(count_bugles(3, 4))
#print(count_bugles(4, 4))
print(count_bugles(4, 5))

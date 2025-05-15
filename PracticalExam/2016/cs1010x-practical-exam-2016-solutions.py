######################################
#   CS1010X AY2014/2015 Semester 2   #
#   Solutions for Practical Exam     #
######################################

#################
# Q1a - Warm Up #
#################

# [ Part A ]

# GRADING SCHEME
#   0 marks if fundamentally wrong or no attempt
#   1-2 marks for the right idea, but still significantly flawed or incomplete
#       (either some attempt at recursion or the approach is somewhat
#        valid but recursion is missing or badly broken)
#   5 marks if generally correct, but
#      -1 mark for any out-of-bounds errors
#      -1 mark for not handling a is shorter than b
#      -1 mark for not handling b completely not in a
#      -1 mark for not handling multiple appearance of digits in the max streak ie, 1121
#      -1 mark if function cannot match one specific length of b
#      -2 marks if function cannot match b when b has more than 1 digit

def contains(a, b): # Recursive version
    if a<b:
        return False
    else:
        count = 0
        tmp = b
        while tmp>0:
            tmp //= 10
            count += 1
        return b==(a%(10**count)) or contains(a//10,b)

def contains(a, b): # Iterative version
    count = 0
    tmp = b
    while tmp>0:
        tmp //= 10
        count += 1
    mask = 10**count
    while a>=b:
        if a%mask == b:
            return True
        a //= 10
    return False

def contains(a, b): # String version >_<
    return str(b) in str(a)

def test1a():
    print('Q1a')
    print(contains(123, 123) == True)
    print(contains(1234, 123) == True)
    print(contains(4123, 123) == True)
    print(contains(123555, 123) == True)
    print(contains(123555, 23) == True)
    print(contains(1243555, 123) == False)

def test1a_private():
    print('Q1a private')

    # True results with exact matches
    print(contains(12345, 12345) == True)
    print(contains(1, 1) == True)
    print(contains(1111111111, 1111111111) == True)

    # True results where multiple instances (overlapping)
    print(contains(1212121, 12) == True)
    print(contains(1212121, 212) == True)
    print(contains(111111, 111) == True)

    # True results with multiple (non-overlapping)
    print(contains(1111111, 1) == True)
    print(contains(1212121212121, 1) == True)
    print(contains(121212333121212, 121212) == True)
    print(contains(123123123, 12) == True)

    # True results palindromic
    print(contains(12321, 123) == True)
    print(contains(12321, 321) == True)

    # False results palindromic
    print(contains(1234321, 124) == False)
    print(contains(1234321, 421) == False)

    # False results where len(b) > len(a)
    print(contains(1234, 12345) == False)
    print(contains(1, 12) == False)

    # False results where len(b) <= len(a)
    print(contains(123456, 8) == False)
    print(contains(1, 8) == False)

#test1a()
#test1a_private()

########################
# Q1b - Longest Streak #
########################

# [ Part B ]

# GRADING SCHEME
#   0 marks if fundamentally wrong or no attempt
#   1-2 marks for the right idea, but still significantly flawed or incomplete
#       (either some attempt at recursion or the approach is somewhat
#        valid but recursion is missing or badly broken)
#   5 marks if generally correct, but
#      -1 mark for semantic error returning the wrong value
#      -1 mark for any out-of-bounds errors
#              including comparing lst[0] and lst[-1] in a streak
#      -1 mark for not handling streaks that only happen in front/middle/rear
#      -1 mark for not handling 1 particular length of number (1 digit, etc)
#      -1 mark for incorrectly adding incontiguous streaks



def count_longest_streak(num): # Recursive version
    if num < 10:
        return 1
    else:
        s = str(num)
        count = 1
        while count < len(s) and s[count] == s[0]:
            count += 1
        if count == len(s):
            return count
        else:
            return max(count,count_longest_streak(int(s[count:])))

def count_longest_streak(num): # Iterative version
    max_count = 0
    s = str(num)
    while s:
        first = s[0]
        count = 1
        while count<len(s) and s[count] == s[0]:
            count += 1
        max_count = max(max_count,count)
        s = s[count:]
    return max_count

def test1b():
    print('Q1b')
    print(count_longest_streak(123456789) == 1)
    print(count_longest_streak(111123456789) == 4)
    print(count_longest_streak(123444456789) == 4)
    print(count_longest_streak(11112211111) == 5)

def test1b_private():
    print('Q1b private')

    # One number
    print(count_longest_streak(1) == 1)
    print(count_longest_streak(9) == 1)

    # Multiple single digits
    print(count_longest_streak(3) == 1)
    print(count_longest_streak(31) == 1)
    print(count_longest_streak(314) == 1)

    # Multiple double digits
    print(count_longest_streak(33) == 2)
    print(count_longest_streak(3311) == 2)
    print(count_longest_streak(331144) == 2)

    # Longest at front
    print(count_longest_streak(112) == 2)
    print(count_longest_streak(11122) == 3)
    print(count_longest_streak(1111222) == 4)

    # Longest at back
    print(count_longest_streak(122) == 2)
    print(count_longest_streak(11222) == 3)
    print(count_longest_streak(1112222) == 4)

    # Longest in the middle
    print(count_longest_streak(1223) == 2)
    print(count_longest_streak(1122233) == 3)
    print(count_longest_streak(1112222333) == 4)

    # Longest multiple parts
    print(count_longest_streak(123) == 1)
    print(count_longest_streak(11233) == 2)
    print(count_longest_streak(112233) == 2)
    print(count_longest_streak(11223311) == 2)
    print(count_longest_streak(1112233311) == 3)
    print(count_longest_streak(11122233) == 3)

    # Longest repeated mutiple streaks (same digit)
    print(count_longest_streak(11221122) == 2)
    print(count_longest_streak(223223) == 2)
    print(count_longest_streak(12231223) == 2)

#test1b()
#test1b_private()

##############################
# Q2 - Stock Market Analysis #
##############################
# DATA Reference : quantquote.com
import csv

def import_csv(filename):
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)

HEADERS = ['date', 'time', 'open', 'high', 'low', 'close', 'volume']
TYPES = [int, int, float, float, float, float, float]

def convert_line(line):
    return tuple(map(lambda i: TYPES[i](line[i]), range(len(line))))

#######################
# Q2a - Minimum Price #
#######################

# [ Part A ]

# GRADING SCHEME
#   0 marks if fundamentally wrong or no attempt
#   0.5 mark for the right idea, but still significantly flawed or incomplete
#       (either some attempt at recursion or the approach is somewhat
#        valid but recursion is missing or badly broken)
#   2 marks if generally correct, but
#      -0.5 mark for clamping on dates outside the range
#      -0.5 mark for not including the start and end date itself
#      -0.5 mark for not filtering the correct start/end time
#      -0.5 mark for not handling empty sequences
#      -0.5 mark for missing out valid rows in the dataset due to incorrect assumption
#           This usually happens when the students *thinks* there's a header row
#      -1 mark for not converting to the correct float type before applying min
#      -1 mark for not using the low column for the solution


def min_stock(filename, start, end):
    data = import_csv(filename)
    data = tuple(map(convert_line, data))
    answer = None
    for date,time,open,high,low,close,volume in data:
        if start <= date <= end:
            if answer == None:
                answer = low
            else:
                answer = min(answer,low)
        if date == end: # Assume data in chronological order
            break
    return answer

EPS = 1e-10
def close(a, b):
    return b-EPS <= a <= b+EPS if type(a) is float or type(a) is int else a == b

def test2a():
    print('Q2a')
    print(close(min_stock("table_tap.csv", 19980218, 19980309), 11.6277))
    print(close(min_stock("table_tap.csv", 19980102, 20130809), 11.0139))
    print(close(min_stock("table_apa.csv", 19980102, 20130809), 6.91758))

def test2a_private():
    print('Q2a private')

    # Constant file
    print(close(min_stock("table_constant.csv", 20150101, 20150201), 0))
    print(close(min_stock("table_constant.csv", 20150101, 20150301), 0))
    print(close(min_stock("table_constant.csv", 20151112, 20151211), 0))

    # Monotonic increase
    print(close(min_stock("table_monoinc.csv", 20150101, 20151231), 1))
    print(close(min_stock("table_monoinc.csv", 20150201, 20151231), 32))
    print(close(min_stock("table_monoinc.csv", 20151001, 20151111), 274))

    # Monotonic Decrease
    print(close(min_stock("table_monodsc.csv", 20150101, 20151231), 1))
    print(close(min_stock("table_monodsc.csv", 20150201, 20151231), 1))
    print(close(min_stock("table_monodsc.csv", 20151001, 20151111), 51))

    # Periodic
    print(close(min_stock("table_periodic1to11.csv", 20150101, 20151231), 1))
    print(close(min_stock("table_periodic1to11.csv", 20150201, 20151231), 1))
    print(close(min_stock("table_periodic1to11.csv", 20151001, 20151111), 1))
    print(close(min_stock("table_periodic1to11.csv", 20150303, 20150310), 3))

    # Date out-of-range
    print(close(min_stock("table_periodic1to11.csv", 20140101, 20141231), None))

    # Date start oor, end in range
    print(close(min_stock("table_constant.csv", 20140101, 20150201), 0))
    print(close(min_stock("table_monoinc.csv", 20140101, 20151231), 1))
    print(close(min_stock("table_monodsc.csv", 20140101, 20151231), 1))
    print(close(min_stock("table_periodic1to11.csv", 20140101, 20151231), 1))

    # Date start in range, end oor
    print(close(min_stock("table_constant.csv", 20150101, 20160201), 0))
    print(close(min_stock("table_monoinc.csv", 20150101, 20161231), 1))
    print(close(min_stock("table_monodsc.csv", 20150101, 20161231), 1))
    print(close(min_stock("table_periodic1to11.csv", 20150101, 20161231), 1))

#test2a()
#test2a_private()


###################
# Q2b  - Volatity #
###################

# [ Part B ]

# GRADING SCHEME
#   0 marks if fundamentally wrong or no attempt
#   1 mark for the right idea, but still significantly flawed or incomplete
#       (either some attempt at recursion or the approach is somewhat
#        valid but recursion is missing or badly broken)
#   3 marks if generally correct, but
#      -0.5 mark for clamping on dates outside the range
#      -0.5 mark for not including the start and end date itself
#      -0.5 mark for not filtering the correct start/end time
#      -0.5 mark for not handling empty sequences
#      -0.5 mark for missing out valid rows in the dataset due to incorrect assumption
#           This usually happens when the students *thinks* there's a header row
#      -1 mark for not using the correct columns for the solution
#      -1 mark for not calculating the average correctly

# We also do not do error carry over. If the same mistake was made in Part(a), we don't
# dock off points for the same problem here. 

def average_daily_variation(filename, start, end):
    data = import_csv(filename)
    data = tuple(map(convert_line, data))
    total = 0
    count = 0
    for date,time,open,high,low,close,volume in data:
        if start <= date <= end:
            total += high-low
            count += 1
        if date == end: # Assume data in chronological order
            break
    return total/count if count > 0 else None

def test2b():
    print('Q2b')
    print(close(average_daily_variation("table_tap.csv", 19980218, 19980309), 0.47104285714285715))
    print(close(average_daily_variation("table_tap.csv", 19980102, 20130809), 0.668375878757002))
    print(close(average_daily_variation("table_apa.csv", 19980102, 20130809), 1.6702794752929195))

def test2b_private():
    print('Q2b private')

    # Constant file
    print(close(average_daily_variation("table_constant.csv", 20150101, 20150201), 0))
    print(close(average_daily_variation("table_constant.csv", 20150101, 20150301), 0))
    print(close(average_daily_variation("table_constant.csv", 20151112, 20151211), 0))

    # Monotonic increase
    print(close(average_daily_variation("table_monoinc.csv", 20150101, 20151231), 1))
    print(close(average_daily_variation("table_monoinc.csv", 20150201, 20151231), 1))
    print(close(average_daily_variation("table_monoinc.csv", 20151001, 20151111), 1))

    # Monotonic Decrease
    print(close(average_daily_variation("table_monodsc.csv", 20150101, 20151231), 1))
    print(close(average_daily_variation("table_monodsc.csv", 20150201, 20151231), 1))
    print(close(average_daily_variation("table_monodsc.csv", 20151001, 20151111), 1))

    # Periodic
    print(close(average_daily_variation("table_periodic1to11.csv", 20150101, 20151231), 1))
    print(close(average_daily_variation("table_periodic1to11.csv", 20150201, 20151231), 1))
    print(close(average_daily_variation("table_periodic1to11.csv", 20151001, 20151111), 1))
    print(close(average_daily_variation("table_periodic1to11.csv", 20150303, 20150310), 1))

    # Date out-of-range
    print(close(average_daily_variation("table_periodic1to11.csv", 20140101, 20141231), None))

    # Date start oor, end in range
    print(close(average_daily_variation("table_constant.csv", 20140101, 20150201), 0))
    print(close(average_daily_variation("table_monoinc.csv", 20140101, 20151231), 1))
    print(close(average_daily_variation("table_monodsc.csv", 20140101, 20151231), 1))
    print(close(average_daily_variation("table_periodic1to11.csv", 20140101, 20151231), 1))

    # Date start in range, end oor
    print(close(average_daily_variation("table_constant.csv", 20150101, 20160201), 0))
    print(close(average_daily_variation("table_monoinc.csv", 20150101, 20161231), 1))
    print(close(average_daily_variation("table_monodsc.csv", 20150101, 20161231), 1))
    print(close(average_daily_variation("table_periodic1to11.csv", 20150101, 20161231), 1))

#test2b()
#test2b_private()


#######################
# Q2c - Optimal Trade #
#######################

# [ Part C ]

# GRADING SCHEME
#   0 marks if fundamentally wrong or no attempt
#   1-2 marks for the right idea, but still significantly flawed or incomplete
#       (either some attempt at recursion or the approach is somewhat
#        valid but recursion is missing or badly broken)
#   5 marks if generally correct, but
#      -0.5 mark for clamping on dates outside the range
#      -0.5 mark for not including the start and end date itself
#      -0.5 mark for not filtering the correct start/end time
#      -0.5 mark for not handling empty sequences / mixing up with 0 max profit
#      -0.5 mark for missing out valid rows in the dataset due to incorrect assumption
#           This usually happens when the students *thinks* there's a header row
#      -1 mark for not using the correct columns for the solution
#      -1 mark for not using absolute difference as the answer
#      -1 mark for not handling best profit that happens within a day
#      -1 marks for off-by-one date errors in buy/sell/ordering
#      -2 marks for ignoring buy/sell order (low must come before high)
#      -2 marks for answer ignoring buying/selling across days
#           Solution only finds best trade in a single day

# Many students just did highest - lowest. This is wrong. Cannot sell before buyer.
# They get 2 points for effort. 

# Quite a number of students got 5/5 for a naive solution that cannot run on Coursemology. 

def trade_stock(datafile, start, end): # Naive approach
    all_data = import_csv(datafile)
    all_data = tuple(map(convert_line,all_data))
    ranged_data = tuple(filter(lambda x:x[0]>=start and x[0]<=end,all_data))

    if ranged_data == ():
        return None

    lows = tuple(map(lambda x:x[4],ranged_data))
    highs = tuple(map(lambda x:x[3],ranged_data))

    max_per_low = []
    for index,low in enumerate(lows): # if we buy at each day's low, what is the max profit we can get from it?
        temp = tuple(map(lambda x:x-low,highs[index:]))
        temp_max = max(temp)
        max_per_low.append(temp_max)

    return max(max_per_low)


def trade_stock(filename, start, end):
    data = import_csv(filename)
    data = tuple(map(convert_line, data))
    seq = []
    for date,time,open,high,low,close,volume in data:
        if start <= date <= end:
            seq.extend((open,low,high,close))
        if date == end: # Assume data in chronological order
            break
    if len(seq) == 0:
        return None
    max_trade = 0
    while seq:
        global_min = 0
        for i in range(len(seq)):
            if seq[i]<seq[global_min]:
                global_min = i
        next_max = global_min
        for i in range(global_min+1,len(seq)):
            if seq[i]>seq[next_max]:
                next_max = i
        max_trade = max(max_trade, seq[next_max] - seq[global_min])
        seq = seq[:global_min]
    return max_trade

def trade_stock(datafile, start, end): # Alternative solution
    converted = list(map(convert_line, import_csv(datafile)))
    data = [x for x in converted if start <= x[0] <= end]
    if len(data) == 0:
        return None
    lows = [x[4] for x in data]
    highs = [x[3] for x in data]

    low = lows[0]
    high = highs[0]
    best = high - low

    for i in range(len(data)):
        if lows[i] < low:
            low = lows[i]
            high = low

        if highs[i] > high:
            high = highs[i]
            best = max(best, high - low)
    return best



def test2c():
    print('Q2c')
    print(close(trade_stock("table_tap.csv", 19980218, 19980309), 1.3630999999999993))
    print(close(trade_stock("table_tap.csv", 19980102, 20130809), 42.7361))
    print(close(trade_stock("table_apa.csv", 19980102, 20130809), 136.89742))
    print(close(trade_stock("table_apa.csv", 20180101, 20181230), None))

    # Test on msft
    print(close(trade_stock("table_msft.csv", 19980205, 20130801), 30.525199999999998))

    # Test clamping
    print(close(trade_stock("table_aapl.csv", 20000101, 20001230), 15.531600000000001))
    print(close(trade_stock("table_aapl.csv", 20000103, 20001229), 15.531600000000001))

    # Test null set
    print(close(trade_stock("table_aapl.csv", 20180101, 20181230), None))

def test2c_private():
    print('Q2c private')
    # Constant file
    print(close(trade_stock("table_constant.csv", 20150101, 20150201), 0))
    print(close(trade_stock("table_constant.csv", 20150101, 20150301), 0))
    print(close(trade_stock("table_constant.csv", 20151112, 20151211), 0))

    # Monotonic increase
    print(close(trade_stock("table_monoinc.csv", 20150101, 20151231), 365))
    print(close(trade_stock("table_monoinc.csv", 20150201, 20151231), 334))
    print(close(trade_stock("table_monoinc.csv", 20151001, 20151111), 42))

    # Monotonic Decrease
    print(close(trade_stock("table_monodsc.csv", 20150101, 20151231), 1))
    print(close(trade_stock("table_monodsc.csv", 20150201, 20151231), 1))
    print(close(trade_stock("table_monodsc.csv", 20151001, 20151111), 1))

    # Periodic
    print(close(trade_stock("table_periodic1to11.csv", 20150101, 20151231), 10))
    print(close(trade_stock("table_periodic1to11.csv", 20150201, 20151231), 10))
    print(close(trade_stock("table_periodic1to11.csv", 20151001, 20151111), 10))
    print(close(trade_stock("table_periodic1to11.csv", 20150303, 20150310), 8))

    # Date out-of-range
    print(close(trade_stock("table_periodic1to11.csv", 20140101, 20141231), None))

    # Date start oor, end in range
    print(close(trade_stock("table_constant.csv", 20140101, 20150201), 0))
    print(close(trade_stock("table_monoinc.csv", 20140101, 20151231), 365))
    print(close(trade_stock("table_monodsc.csv", 20140101, 20151231), 1))
    print(close(trade_stock("table_periodic1to11.csv", 20140101, 20151231), 10))

    # Date start in range, end oor
    print(close(trade_stock("table_constant.csv", 20150101, 20160201), 0))
    print(close(trade_stock("table_monoinc.csv", 20150101, 20161231), 365))
    print(close(trade_stock("table_monoinc.csv", 20150101, 20161231), 365))
    print(close(trade_stock("table_monodsc.csv", 20150101, 20161231), 1))
    print(close(trade_stock("table_periodic1to11.csv", 20150101, 20161231), 10))


#test2c()
#test2c_private()


#####################
# Q3 - Going Places #
#####################

# GRADING SCHEME
#   0 marks if fundamentally wrong or no attempt
#   1-2 marks for the right idea, but still significantly flawed or incomplete
#       (either some attempt at recursion or the approach is somewhat
#        valid but recursion is missing or badly broken)
#   10 marks if generally correct, but
#    [add_node]
#      -1 mark for not handling duplicate nodes correctly
#           This is subject to how the rest of the functions deal with the duplicates as well
#      -2 marks for non-functioning solution
#    [add_link]
#      -1 mark for not handling invalid nodes
#    [get_distance]
#      -0.5 mark for returning None in False cases
#      -1 mark for not handling invalid nodes
#      -1 mark for not handling bidirectional connections
#      -2 marks for not handling nodes that are not adjacent
#    [get_paths]
#      -1 mark for not handling nodes that are disconnected or invalid
#      -1 mark for not returning all possible paths
#      -1 mark for not handling paths longer than direct connections from src to target
#    [shortest_path]
#      -1 mark for not handling nodes that are disconnected or invalid
#      -1 mark for not handling paths in reverse of added links
#      -1 mark if path returned is not the minimum distance path




class Node: # Helper node object
    def __init__(self, name):
        self.name = name
        self.neighbours = {}

    def add_neighbour(self, n, dist):
        if n not in self.neighbours:
            self.neighbours[n] = dist
        if self not in n.neighbours:
            n.neighbours[self] = dist

    def get_distance(self, n):
        if n not in self.neighbours:
            return False
        else:
            return self.neighbours[n]

    def get_neighbours(self):
        return list(map(lambda n: n.name, self.neighbours.keys()))

class Map:
    def __init__(self):
        self.nodes = {}

    def add_node(self,name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)

    def add_link(self,a,b,dist):
        if a not in self.nodes or b not in self.nodes:
            return False
        self.nodes[a].add_neighbour(self.nodes[b],dist)
        return True

    def get_distance(self, a, b):
        if a not in self.nodes or b not in self.nodes:
            return False
        else:
            return self.nodes[a].get_distance(self.nodes[b])

    def get_paths(self,a,b):
        if a not in self.nodes or b not in self.nodes:
            return []
        paths = []
        tocheck = [[a]]
        while tocheck:
            current = tocheck.pop()
            next_step = self.nodes[current[-1]].get_neighbours()
            for n in next_step:
                if n not in current:
                    temp = current.copy()
                    temp.append(n)
                    if n == b:
                        paths.append(temp)
                    else:
                        tocheck.append(temp)
        return paths

    def shortest_path(self,a,b):
        if a not in self.nodes or b not in self.nodes:
            return False
        paths = self.get_paths(a,b)
        if not paths:
            return False

        def compute(path):
            dist = 0
            for i in range(len(path)-1):
                dist += self.get_distance(path[i],path[i+1])
            return dist

        min_path = compute(paths[0])
        for path in paths[1:]:
            min_path = min(min_path,compute(path))
        return min_path


def sortall(lst):
    return sorted(list(map(sortall, lst))) if type(lst) is list else lst

def test3():
    m = Map()
    m.add_node("Singapore")
    m.add_node("Seoul")
    m.add_node("San Francisco")
    m.add_node("Tokyo")
    m.add_link("Tokyo","Seoul",1152)
    m.add_link("Singapore","Seoul",4669)
    m.add_link("Singapore","Tokyo",5312)
    m.add_link("Tokyo","San Francisco",5136)

    print("Q3")
    print(sortall(m.get_paths("Singapore","Seoul")) ==\
            sortall([['Singapore', 'Seoul'], ['Singapore', 'Tokyo', 'Seoul']]))

    print(sortall(m.get_paths("San Francisco","Seoul")) ==\
            sortall([['San Francisco', 'Tokyo', 'Seoul'],\
            ['San Francisco', 'Tokyo', 'Singapore', 'Seoul']]))

    print(sortall(m.get_paths("Seoul","San Francisco")) ==\
            sortall([['Seoul', 'Tokyo', 'San Francisco'],\
            ['Seoul', 'Singapore', 'Tokyo', 'San Francisco']]))

    print(m.shortest_path("Singapore","Seoul") == 4669)
    print(m.shortest_path("San Francisco","Seoul") == 6288)
    print(m.shortest_path("Seoul","San Francisco") == 6288)


def test3_private():
    print('Q3 private')
    # Disconnected graph
    m = Map()
    m.add_node('1')
    m.add_node('2')
    m.add_node('3')
    m.add_node('4')
    m.add_node('5')

    # Null set, no paths
    print(sortall(m.get_paths('1', '2')) == [])
    print(sortall(m.get_paths('1', '5')) == [])
    print(sortall(m.get_paths('4', '5')) == [])

    # Null set, invalid nodes
    print(sortall(m.get_paths('-1', '2')) == [])
    print(sortall(m.get_paths('1', '8')) == [])
    print(sortall(m.get_paths('t', '5')) == [])

    # False, no distance
    print(sortall(m.get_distance('1', '2')) == False)
    print(sortall(m.get_distance('3', '4')) == False)
    print(sortall(m.get_distance('4', '5')) == False)

    # False, invalid nodes
    print(sortall(m.get_distance('1', '-2')) == False)
    print(sortall(m.get_distance('-3', '4')) == False)
    print(sortall(m.get_distance('4', 'z')) == False)

    # False, no shortest path
    print(sortall(m.shortest_path('1', '2')) == False)
    print(sortall(m.shortest_path('1', '5')) == False)
    print(sortall(m.shortest_path('4', '5')) == False)

    # False, invalid nodes
    print(sortall(m.shortest_path('1', '-2')) == False)
    print(sortall(m.shortest_path('-3', '4')) == False)
    print(sortall(m.shortest_path('4', 'z')) == False)


    # Linear Chain
    # 1 - 2 - 3 - 4 - 5
    m.add_link('1', '2', 1)
    m.add_link('2', '3', 1)
    m.add_link('3', '4', 1)
    m.add_link('4', '5', 1)

    # Single path
    print(sortall(m.get_paths('1', '2')) == [['1', '2']])
    print(sortall(m.get_paths('1', '4')) == [['1', '2', '3', '4']])
    print(sortall(m.get_paths('2', '5')) == [['2', '3', '4', '5']])

    # Distance (forward)
    print(m.get_distance('1', '2') == 1)
    print(m.get_distance('2', '3') == 1)
    print(m.get_distance('4', '5') == 1)

    # Distance (reverse)
    print(m.get_distance('5', '4') == 1)
    print(m.get_distance('4', '3') == 1)
    print(m.get_distance('2', '1') == 1)

    # Distance (not adjacent)
    print(m.get_distance('1', '4') == False)
    print(m.get_distance('4', '1') == False)
    print(m.get_distance('2', '7') == False)
    print(m.get_distance('2', '-1') == False)

    # Shortest path (forward)
    print(m.shortest_path('1', '2') == 1)
    print(m.shortest_path('2', '4') == 2)
    print(m.shortest_path('1', '5') == 4)

    # Shortest path (reverse)
    print(m.shortest_path('2', '1') == 1)
    print(m.shortest_path('4', '2') == 2)
    print(m.shortest_path('5', '1') == 4)

    # Shortest path, invalid nodes
    print(m.shortest_path('-2', '1') == False)
    print(m.shortest_path('7', '-2') == False)
    print(m.shortest_path('t', '1') == False)


    # Ring
    # 1 - 2 - 3
    # |       |
    # 5 ----- 4
    m.add_link('5', '1', 1)

    # Single path
    print(sortall(m.get_paths('1', '2')) == sortall([['1', '2'], ['1', '5', '4', '3', '2']]))
    print(sortall(m.get_paths('1', '4')) == sortall([['1', '2', '3', '4'], ['1', '5', '4']]))
    print(sortall(m.get_paths('2', '5')) == sortall([['2', '1', '5'], ['2', '3', '4', '5']]))

    # Distance (forward)
    print(m.get_distance('1', '2') == 1)
    print(m.get_distance('2', '3') == 1)
    print(m.get_distance('4', '5') == 1)
    print(m.get_distance('5', '1') == 1)

    # Distance (reverse)
    print(m.get_distance('5', '4') == 1)
    print(m.get_distance('4', '3') == 1)
    print(m.get_distance('2', '1') == 1)
    print(m.get_distance('1', '5') == 1)

    # Distance (not adjacent)
    print(m.get_distance('1', '4') == False)
    print(m.get_distance('4', '1') == False)
    print(m.get_distance('2', '7') == False)
    print(m.get_distance('2', '-1') == False)

    # Shortest path
    print(m.shortest_path('1', '2') == 1)
    print(m.shortest_path('2', '4') == 2)
    print(m.shortest_path('1', '5') == 1)
    print(m.shortest_path('2', '1') == 1)
    print(m.shortest_path('4', '2') == 2)
    print(m.shortest_path('5', '1') == 1)

    # Shortest path, invalid nodes
    print(m.shortest_path('-2', '1') == False)
    print(m.shortest_path('7', '-2') == False)
    print(m.shortest_path('t', '1') == False)

#test3()
#test3_private()


import csv

##############
# Question 1 #
##############

#################
# Q1a - Warm Up #
#################

def contains(a, b):
    # Write your solution here
    pass

def test1a():
    print('Q1a')
    print(contains(123, 123) == True)
    print(contains(1234, 123) == True)
    print(contains(4123, 123) == True)
    print(contains(123555, 123) == True)
    print(contains(123555, 23) == True)
    print(contains(1243555, 123) == False)

#test1a()



########################
# Q1b - Longest Streak #
########################

def count_longest_streak(a):
    # Write your solution here
    pass

def test1b():
    print('Q1b')
    print(count_longest_streak(123456789) == 1)
    print(count_longest_streak(111123456789) == 4)
    print(count_longest_streak(123444456789) == 4)
    print(count_longest_streak(11112211111) == 5)

#test1b()



##############################
# Q2 - Stock Market Analysis #
##############################
# These functions are provided for you
# Do not make any changes to them

def import_csv(filename):
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)


#######################
# Q2a - Minimum Price #
#######################

def min_stock(datafile, start, end):
    # Write your solution here
    pass

EPS = 1e-10 # For approximation of floating point answers
def close(a, b):
    return b-EPS <= a <= b+EPS

def test2a():
    print('Q2a')
    print(close(min_stock("table_tap.csv", 19980218, 19980309), 11.6277))
    print(close(min_stock("table_tap.csv", 19980102, 20130809), 11.0139))
    print(close(min_stock("table_apa.csv", 19980102, 20130809), 6.91758))

#test2a()


##################
# Q2b - Volatity #
##################

def average_daily_variation(datafile, start, end):
    # Write your solution here
    pass

def test2b():
    print('Q2b')
    print(close(average_daily_variation("table_tap.csv", 19980218, 19980309), 0.47104285714285715))
    print(close(average_daily_variation("table_tap.csv", 19980102, 20130809), 0.668375878757002))
    print(close(average_daily_variation("table_apa.csv", 19980102, 20130809), 1.6702794752929195))

#test2b()


#######################
# Q2c - Optimal Trade #
#######################

def trade_stock(datafile, start, end):
    # Write your solution here
    pass

def test2c():
    print('Q2c')
    print(close(trade_stock("table_tap.csv", 19980218, 19980309), 1.3630999999999993))
    print(close(trade_stock("table_tap.csv", 19980102, 20130809), 42.7361))
    print(close(trade_stock("table_apa.csv", 19980102, 20130809), 136.89742))

    # Test null set
    print(trade_stock("table_apa.csv", 20180101, 20181230)==None)

#test2c()


#####################
# Q3 - Going Places #
#####################

class Map():
    # Write your solution here
    pass


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

    def sortall(lst):
        return sorted(list(map(sortall, lst))) if type(lst) is list else lst

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

#test3()

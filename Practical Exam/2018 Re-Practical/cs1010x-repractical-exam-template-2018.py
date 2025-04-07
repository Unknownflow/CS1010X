import csv
from math import sqrt

##############
# Question 1 #
##############


##################################
# Q1a - Is right angle triangle? #
##################################

def pythagoras(a,b,c):
    pass
    
def test1a():
    print('=== Q1a ===')
    print(pythagoras((0,0),(1,2),(1,1))==False)
    print(pythagoras((0,0),(1,0),(0,1))==True)
    print(pythagoras((0,0),(2,0),(0,2))==True)
   
#test1a()

#########################
# Q1b - Count triangles #
#########################

def count_triangles(lst):
    pass
    
def test1b():
    print('=== Q1b ===')
    print(count_triangles(((0,0),(1,0),(0,1)))==1)
    print(count_triangles(((0,0),(1,1),(2,1)))==0)
    print(count_triangles(((0,0),(1,0),(0,1),(-1,-2)))==2)  # [[(0, 0), (1, 0), (0, 1)], [(1, 0), (0, 1), (-1, -2)]]
    print(count_triangles(((0,0),(1,0),(0,1),(1,1)))==4)

#test1b()
 
###########################
# Q2 - Finding Happiness  #
###########################
# These functions are provided for you
# Do not make any changes to them
def approx(a,b):
    return (a-b)*(a-b)<0.0000001

def read_csv(filename):  # provided
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)
 
#######
# Q2A #
#######

stats = ['GDP', 'Social', 'HLE', 'Freedom', 'Generosity']

def parse_data(filename):
    pass

def test2a():
    print('=== Q2a ===')
    report = parse_data("happiness.csv")
    print(approx(report[2017]['India']['Social'], 0.6067674756) == True)
    print(approx(report[2013]['Singapore']['GDP'], 11.2714776993) == True)
    print(approx(report[2014]['Brazil']['Generosity'], -0.1286974549) == True)
    print(approx(report[2008]['Austria']['Freedom'], 0.8790692687) == True)
    print(approx(report[2011]['Chile']['HLE'], 68.6461639404) == True)
    try:
        report[2007]['Canada']['Social']
    except KeyError as e:
        print(e) # 'Social'

#test2a()

#######
# Q2B #
#######
def get_all_countries(data_map):
    countries = []
    for v in data_map.values():
        for k in v.keys():
            if k not in countries:
                countries.append(k)
    return countries

def get_countries(filename,*conditions):
    pass

## Tests ##
def test2b():
    print('=== Q2b ===')
    print(get_countries("happiness.csv", lambda y, c: y >= 2012 and c['GDP'] > 11, lambda y, c: y == 2011 and c['Social'] > 0.9)==['Ireland', 'Singapore', 'Luxembourg']) 
    print(get_countries("happiness.csv", lambda y, c: y == 2012 and c['GDP'] > 11, lambda y, c: y == 2011 and c['Social'] > 0.9)==['Luxembourg']) 
    print(get_countries("happiness.csv", lambda y, c: y > 2020 and c['GDP'] > 0)==[]) 

#test2b()

#######
# Q2C #
#######
def predict(filename, country, metric, year):
    pass
 
## Tests ##
def test2c():
    print('=== Q2c ===')
    print(approx(predict("happiness.csv", "Japan", "GDP", 2050), 10.786426327185783) == True) 
    print(approx(predict("happiness.csv", "Italy", "Social", 2030), 0.9245298996310285) == True)
    print(approx(predict("happiness.csv", "Nigeria", "Generosity", 2019), 0.018709013077190306) == True) 
     
#test2c()

#########################
# Q3 - Trump-Kim Summit #
#########################

class TripPlanner:

    def __init__(self, filename):
        # add your code here

        # Do not modify this line.
        self.read(filename)       
    
    def read(self, filename):   # Provided Helper - do not modify
        data = read_csv(filename)
        for line in data:
            if line[0] == "JOIN":
                to_add = list(filter(lambda x: x !="", line[1:]))
                self.add_junction(*to_add)
            elif line[0] == "BUILDING":
                self.add_place(line[1],line[2])
            else:
                print("Error:", line)

## Tests ##
def test3():
    print('=== Q3 ===')
    t = TripPlanner("orchard.csv")
    print(t.can_reach('Gleneagles Hospital', 'St Regis')==True)
    print(t.can_reach('Four Seasons', 'St Regis')==True)
    print(t.can_reach('M&S', 'St Regis')==True)
    print(t.can_reach('Marriot', 'St Regis')==True)
    print(t.can_reach('Shangri La', 'St Regis')==True)
    print(t.is_connected('Tanglin Road', 'Orchard Road A')==True)
    print(t.is_connected('Tanglin Road', 'Paterson Road')==False)
    print(t.get_road('Shangri La')=="Orange Grove Road")
    
    print(t.block_road('Cuscaden Road')==True)
    print(t.block_road('Cuscaden Road')==False)
    print(t.can_reach('Gleneagles Hospital', 'St Regis')==False)
    print(t.can_reach('Four Seasons', 'St Regis')==False)
    print(t.can_reach('M&S', 'St Regis')==False)
    print(t.can_reach('Marriot', 'St Regis')==False)
    print(t.can_reach('Shangri La', 'St Regis')==False)

    print(t.unblock_road('Cuscaden Road')==True)
    print(t.unblock_road('Cuscaden Road')==False)
    print(t.can_reach('Shangri La', 'St Regis')==True)
    print(t.block_road('Orange Grove Road')==True)
    print(t.can_reach('Shangri La', 'St Regis')==False)
    print(t.can_reach('Gleneagles Hospital','Marriot')==True)

# test3()

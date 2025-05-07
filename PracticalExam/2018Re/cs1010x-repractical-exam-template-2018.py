import csv
from math import sqrt

##############
# Question 1 #
##############


##################################
# Q1a - Is right angle triangle? #
##################################

def pythagoras(a,b,c):
    def dist_squared(pt1, pt2):
        x1 = pt1[0]
        x2 = pt2[0]
        y1 = pt1[1]
        y2 = pt2[1]
        return (x1-x2) ** 2 + (y1-y2) ** 2
    
    dist1 = dist_squared(a, b) 
    dist2 = dist_squared(a, c) 
    dist3 = dist_squared(b, c) 

    if dist1 + dist2 == dist3 or \
       dist2 + dist3 == dist1 or \
       dist3 + dist1 == dist2:
        
        return True
    else:
        return False

    
        
    
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
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                if pythagoras(lst[i], lst[j], lst[k]):
                    count += 1
    
    return count
    
    
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
    lines = read_csv(filename)
    res = {}
    
    for line in lines[1:]:
        country = line[0]
        year = int(line[1])
        line_data = {}

        if line[2] != "":
            line_data["GDP"] = float(line[2])

        if line[3] != "":
            line_data["Social"] = float(line[3])

        if line[4] != "":
            line_data["HLE"] = float(line[4])

        if line[5] != "":
            line_data["Freedom"] = float(line[5])

        if line[6] != "":
            line_data["Generosity"] = float(line[6])

        if year not in res:
            res[year] = {country: line_data}
        else:
            res[year][country] = line_data

    return res

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
    data = parse_data(filename)
    countries = []
    
    for year, countries_data in data.items():
        for country in countries_data.keys():
            if country not in countries:
                countries.append(country)

                
    if len(conditions) == 0:
        return countries
    else:
        countries_fulfilled = []
        for i in range(len(conditions)):
            condition = conditions[i]
            countries_fulfilled.append([])

            for year, countries_data in data.items():
                for country, country_info in countries_data.items():
                    #print(year, country_info)
                    try:
                        #print(condition(year, country_info))
                        if condition(year, country_info):
                            countries_fulfilled[i].append(country)
                    except KeyError:
                        continue
        countries = []
        for country in countries_fulfilled[0]:
            common = True
            
            for i in range(1, len(countries_fulfilled)):
                if country not in countries_fulfilled[i]:
                    common = False
                    break
            if common and country not in countries:
                countries.append(country)
        countries.sort(key = lambda x: str(x))
        print(countries)
        return countries

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
    data = parse_data(filename)
    sum_y = 0
    sum_x = 0
    sum_x_sq = 0
    sum_xy = 0
    n = 0
    for year_, countries_data in data.items():
        if country in countries_data:
            if metric in countries_data[country]:
                sum_x += year_
                sum_x_sq += year_ * year_
                sum_y += countries_data[country][metric]
                sum_xy += year_ * countries_data[country][metric]
                n += 1
        
    if n == 0:
        return None
    a = (sum_y * sum_x_sq - sum_x * sum_xy) / (n * sum_x_sq - (sum_x) ** 2)
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sq - (sum_x) ** 2)

    return a + b * year
    
     
## Tests ##
def test2c():
    print('=== Q2c ===')
    print(approx(predict("happiness.csv", "Japan", "GDP", 2050), 10.786426327185783) == True) 
    print(approx(predict("happiness.csv", "Italy", "Social", 2030), 0.9245298996310285) == True)
    print(approx(predict("happiness.csv", "Nigeria", "Generosity", 2019), 0.018709013077190306) == True) 
     
test2c()

#########################
# Q3 - Trump-Kim Summit #
#########################

class TripPlanner:

    def __init__(self, filename):
        # add your code here
        self.roads_connection = {}
        self.places = {}

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

    def add_junction(self, *roads):
        for road1 in roads:
            if road1 not in self.roads_connection:
                self.roads_connection[road1] = {"blocked": False, "roads": []}

            for road2 in roads:
                if road1 != road2:
                    self.roads_connection[road1]["roads"].append(road2)
        return

    def add_place(self, place, road):
        if road in self.roads_connection:
            self.roads_connection[road]["roads"].append(place)
            self.places[place] = road
        return

    def is_connected(self, road1, road2):
        if road1 in self.roads_connection:
            if self.is_blocked(road1) or self.is_blocked(road2):
                return False
            for road in self.roads_connection[road1]["roads"]:
                if road == road2:
                    return True
            return False
        else:
            return "No such road"

    def get_road(self, place):
        if place in self.places:
            return self.places[place]
        else:
            return "No such place"

    def block_road(self, road):
        if road in self.roads_connection:
            if self.roads_connection[road]["blocked"] == True:
                return False
            else:
                self.roads_connection[road]["blocked"] = True
                return True
        else:
            return "No such road"

    def unblock_road(self, road):
        if road in self.roads_connection:
            if self.roads_connection[road]["blocked"] == True:
                self.roads_connection[road]["blocked"] = False
                return True
            else:
                return False
        else:
            return "No such road"

    def is_blocked(self, road):
        if road in self.roads_connection:
            if self.roads_connection[road]["blocked"] == True:
                return True
            else:
                return False
        else:
            return False

    def can_reach(self, place1, place2):
        road1 = self.get_road(place1)
        road2 = self.get_road(place2)
        if road1 == "No such place" or road2 == "No such place":
            return "No such place"
        if self.is_connected(road1, road2):
            return True
        else:
            if self.is_blocked(road1) or self.is_blocked(road2):
                return False
            possible_roads = []

            for road in self.roads_connection[road1]["roads"]:
                possible_roads.append(road)

            while possible_roads:
                road = possible_roads.pop()
                if self.is_connected(road, road2):
                    return True

            return False

    
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

#test3()

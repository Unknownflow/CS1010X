from math import *


###############
# Question 1a #
###############
def smallest(*lst):
    lst = sorted(lst)

    # first number cannot be 0, must find smallest number (not 0) to replace it
    if lst[0] == 0:
        zero_count = 0
        # count num of 0 in the lst
        for num in lst:
            if num == 0:
                zero_count += 1
        smallest_num = lst[zero_count]
        zero_lst = [0 for i in range(zero_count)]
        # smallest number will be (smallest num in lst) + zeros + rest of numbers
        lst = [smallest_num] + zero_lst + lst[zero_count+1:]

    # calculate the result base on num in the lst
    res = 0
    for i in range(0, len(lst)):
        res *= 10
        res += lst[i]
    return res


def test1a():
    print('=== Q1a ===')
    print(smallest(9,1,3)==139)
    print(smallest(1,3,9,0,0)==10039)
    print(smallest(2,1,1,3,9,0)==101239)
 
# test1a() 

###############
# Question 1b #
###############
def second_smallest(*lst):
    lst = sorted(lst)
    # no possible integer
    first = lst[0]
    diff = False
    for num in lst:
        if num != first:
            diff = True
    
    if not diff:
        return None
    
        # first number cannot be 0, must find smallest number (not 0) to replace it
    if lst[0] == 0:
        zero_count = 0
        # count num of 0 in the lst
        for num in lst:
            if num == 0:
                zero_count += 1
        smallest_num = lst[zero_count]
        zero_lst = [0 for i in range(zero_count)]
        # smallest number will be (smallest num in lst) + zeros + rest of numbers
        lst = [smallest_num] + zero_lst + lst[zero_count+1:]

    # if lst 2 items in arr is not equal to each other
    # for i in range(zero_count+1, len(lst)-1):
    #     if lst[i]

    #     lst[idx], lst[-1] = lst[-1], lst[idx]
    #     print(lst)

    # calculate the result base on num in the lst
    res = 0
    for i in range(0, len(lst)):
        res *= 10
        res += lst[i]
    return res
    


def test1b():
    print('=== Q1b ===')
    print(second_smallest(9,1,3)==193)
    print(second_smallest(1,3,9,0,0)==10093)
    print(second_smallest(2,1,1,3,9,0)==101293)
    print(second_smallest(1, 0, 1, 1, 2, 2, 2))
    print(second_smallest(1,1,1)==None)
     
# test1b() 

##############
# Question 2 #
##############

import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

###############
# Question 2a #
###############

def most_common_major(filename, year):
    max_grads = 0
    most_grads_course = ""
    with open(filename, "r") as f:
        f.readline()
        for line in f:
            line = line.strip("\n").split(",")
            year_data = int(line[0])
            gender = line[1] 
            course = " ".join(line[2:-1])
            num_grads = line[-1] 
            # invalid data
            if num_grads == "na":
                continue
            # year found
            if year == year_data:
                num_grads = int(num_grads)
                # more common major found
                if num_grads > max_grads:
                    max_grads = num_grads
                    most_grads_course = course

    return most_grads_course

def test2a():
    print('=== Q2a ===')
    print(most_common_major("graduates-by-first-degree.csv", 1993)=="Engineering Sciences")
    print(most_common_major("graduates-by-first-degree.csv", 2000)=="Engineering Sciences")
    print(most_common_major("graduates-by-first-degree.csv", 2010)=="Engineering Sciences")

# test2a()

###############
# Question 2b #
###############

def new_courses(filename,start_year,end_year):
    courses = {}
    with open(filename, "r") as f:
        f.readline()
        for line in f:
            line = line.strip("\n").split(",")
            year_data = int(line[0])
            gender = line[1] 
            course = " ".join(line[2:-1])
            num_grads = line[-1] 
            # year within range
            if start_year <= year_data <= end_year:
                # if no enrollment
                if num_grads == "na":
                    courses[course] = "na"
                else:
                    if course in courses:
                        # if there is course data n is a new course, replace na with start year
                        if courses[course] == "na" and int(num_grads) > 0:
                            courses[course] = year_data
    
    res = []
    for key, val in courses.items():
        if val != "na": # only new courses with enrollment added
            res.append((key, val))
    
    # sort by year
    return sorted(res, key=lambda x: x[1])

def test2b():
    print('=== Q2b ===')
    print(new_courses("graduates-by-first-degree.csv",1993,2000)==[('Education', 1995), ('Mass Communication', 1997)]
)
    print(new_courses("graduates-by-first-degree.csv",2001,2010)==[('Applied Arts', 2003), ('Services', 2008)]
)
    print(new_courses("graduates-by-first-degree.csv",1993,2020)==[('Education', 1995), ('Mass Communication', 1997), ('Applied Arts', 2003), ('Services', 2008)])

# test2b()

###############
# Question 2c #
###############

def topk_growing_major(filename,k,start_year,end_year):
    courses = {}
    with open(filename, "r") as f:
        f.readline()
        for line in f:
            line = line.strip("\n").split(",")
            year_data = int(line[0])
            gender = line[1] 
            course = " ".join(line[2:-1])
            num_grads = line[-1] 

            if num_grads == "na":
                continue
            num_grads = int(num_grads)
            if start_year == year_data:
                if course in courses:
                    courses[course][0] += num_grads
                else:
                    courses[course] = [num_grads,0]
            if end_year == year_data:
                if course in courses:
                    courses[course][1] += num_grads
                else:
                    courses[course] = [0,num_grads]
    
    res = []
    for key, val in courses.items():
        start_year_num = val[0]
        end_year_num = val[1]
        if start_year_num != 0:
            percentage_change = (end_year_num - start_year_num) / start_year_num
            res.append((key, percentage_change))

    res = sorted(res, key=lambda x: x[1], reverse=True)
    output = []
    for i in range(k):
        output.append(res[i][0])
    return output

def test2c():
    print('=== Q2c ===')
    print(topk_growing_major("graduates-by-first-degree.csv",3,1993,2000)==['Engineering Sciences', 'Dentistry', 'Humanities & Social Sciences']
)
    print(topk_growing_major("graduates-by-first-degree.csv",2,2000,2010)==['Health Sciences', 'Education'])
    print(topk_growing_major("graduates-by-first-degree.csv",3,2000,2014)==['Health Sciences', 'Education', 'Law'])

# test2c()
    
##############
# Question 3 #
##############

class Timeline:
    def __init__(self):
        self.people = []
    
    def born(self, name, year, lifespan):
        person = Person(name, year, lifespan)
        self.people.append(person)
        return person

    def get_people(self, year):
        res = []
        for people in self.people:
            for identity, person in people.get_identities().items():
                person_year = person.get_year()
                lifespan = person.get_lifespan()
                if person_year <= year and year < person_year + lifespan:
                    if year < person.get_dead_from():
                        res.append((person.get_name(), identity))
                # print('personb4', person.__str__(), person_year, lifespan)
                person = person.get_name()
            
            person = people
            person_year = person.get_year()
            lifespan = person.get_lifespan()
            if person_year <= year and year < person_year + lifespan:
                if year < person.get_dead_from():
                    res.append(person.__str__())
            # print('personb4', person.__str__(), person_year, lifespan)
            person = person.get_name()
        return res
        

class Person:
    def __init__(self, name, year, lifespan):
        self.name = name
        self.year = year
        self.lifespan = lifespan
        self.dead_from = inf
        self.identities = {}

    def jump(self, from_year, to_year, identity):
        if self.identities == {}:
            self.lifespan = from_year - self.get_year()
        if identity in self.identities:
            curr_identity = self.identities[identity]
            curr_identity.lifespan = from_year - curr_identity.get_year()
        new_person = Person(self.get_name(), to_year, self.get_lifespan())
        self.identities[from_year] = new_person
    
    def kill(self, year, person, identity):
        if self.get_year() <= year <= self.get_year() + self.get_lifespan():
            person_year = person.get_year()
            if person_year != identity:
                # not the same person
                return False
            else:
                # if the person is alive kill him
                if person.dead_from == inf and person.get_year() <= year <= person.get_year() + person.get_lifespan():
                    # replace year with na
                    person.dead_from = year
                    return True
                else:
                    return False
        else:
            # killer not around in the time
            return False
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def get_lifespan(self):
        return self.lifespan
    
    def set_lifespan(self, lifespan):
        self.lifespan = lifespan

    def get_identities(self):
        return self.identities
    
    def get_dead_from(self):
        return self.dead_from
    
    def __str__(self):
        return (self.name, self.year)

def test3():
    print('=== Q3 ===')
    t = Timeline()
    thor = t.born("Thor",518,5000)
    thanos = t.born("Thanos",1950,1000000)

    print(t.get_people(2017)==[('Thor', 518), ('Thanos', 1950)])
    print(thor.kill(2018,thanos,1950)) # whoops. Violence. :'(
    print(not thor.kill(2018,thanos,1950)) # Can't kill him twice!
    print(t.get_people(2018)==[('Thor', 518)]) # Thanos dead.
    
    thor.jump(2023,2013,518)
    thor.jump(2014,2024,2023)

    print(set(t.get_people(2013))==set([('Thor', 2023), ('Thor', 518), ('Thanos', 1950)]))
    print(set(t.get_people(2014))==set([('Thor', 518), ('Thanos', 1950)]))

    print(t.get_people(2022)==[('Thor', 518)])
    print(t.get_people(2023)==[])
    print(t.get_people(2024)==[('Thor', 2014)])

    thanos.jump(2014,2024,1950)
    print(set(t.get_people(2024))==set([('Thor', 2014), ('Thanos', 2014)]))

    # New Thor and old Thanos jumped so only old Thor left
    print(t.get_people(2014)==[('Thor', 518)]) 
    print(t.get_people(2017)==[('Thor', 518)])

    #Thanos is no longer around to die. 
    print(not thor.kill(2018,thanos,1950))


# test3()


             

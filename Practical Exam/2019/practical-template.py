from math import *


###############
# Question 1a #
###############
def smallest(*lst):
    pass


def test1a():
    print('=== Q1a ===')
    print(smallest(9,1,3)==139)
    print(smallest(1,3,9,0,0)==10039)
    print(smallest(2,1,1,3,9,0)==101239)
 
#test1a() 

###############
# Question 1b #
###############
def second_smallest(*lst):
    pass

def test1b():
    print('=== Q1b ===')
    print(second_smallest(9,1,3)==193)
    print(second_smallest(1,3,9,0,0)==10093)
    print(second_smallest(2,1,1,3,9,0)==101293)
    print(second_smallest(1,1,1)==None)
     
#test1b() 

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
    pass

def test2a():
    print('=== Q2a ===')
    print(most_common_major("graduates-by-first-degree.csv", 1993)=="Engineering Sciences")
    print(most_common_major("graduates-by-first-degree.csv", 2000)=="Engineering Sciences")
    print(most_common_major("graduates-by-first-degree.csv", 2010)=="Engineering Sciences")

#test2a()

###############
# Question 2b #
###############

def new_courses(filename,start_year,end_year):
    pass

def test2b():
    print('=== Q2b ===')
    print(new_courses("graduates-by-first-degree.csv",1993,2000)==[('Education', 1995), ('Mass Communication', 1997)]
)
    print(new_courses("graduates-by-first-degree.csv",2001,2010)==[('Applied Arts', 2003), ('Services', 2008)]
)
    print(new_courses("graduates-by-first-degree.csv",1993,2020)==[('Education', 1995), ('Mass Communication', 1997), ('Applied Arts', 2003), ('Services', 2008)])

#test2b()

###############
# Question 2c #
###############

def topk_growing_major(filename,k,start_year,end_year):
    pass

def test2c():
    print('=== Q2c ===')
    print(topk_growing_major("graduates-by-first-degree.csv",3,1993,2000)==['Engineering Sciences', 'Dentistry', 'Humanities & Social Sciences']
)
    print(topk_growing_major("graduates-by-first-degree.csv",2,2000,2010)==['Health Sciences', 'Education'])
    print(topk_growing_major("graduates-by-first-degree.csv",3,2000,2014)==['Health Sciences', 'Education', 'Law'])

#test2c()
    
##############
# Question 3 #
##############

class Timeline:

    pass
        

class Person:

    pass

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


#test3()


             

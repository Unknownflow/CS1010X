# use Python tutor on 4 screens - to show the box and pointer diagram
#
# tuple is immutable - cannot be changed
# need to pay for every single one that we update

#######################
# in python tutor    #1: working with tuple, and working with list
#######################
t = (1,2,(3,4), 3)
print(len(t))
s = t
print(id(s)==id(t))
print("id of s:", id(s))
t = t + (4,)
print("id of t:", id(t))

print("id of t[2]", id(t[2]))
print("id of s[2]", id(s[2]))
print(id(t[2]) == id(s[2]))

print("s is", s, "and its id", id(s))
print("t is", t, "and its id", id(t))
print(id(s) == id(t))

# list is different

k = [1,2,3, [1,3], 4]
m = k
k.append(5)   # this is in place append
print(id(m) == id(k))
m = m + [4]   # this is not in place append

k += [4]       # this statement is not quite k = k + [4], but 
               # telling the interpreter to be smarter in knowing 
               # that interpreter (it) should re-use the old k

print(id(m) == id(k))
print(id(m[3]) == id(k[3]))



# python tutor #2
# becareful function manipulation
#######################
# in python tutor    #2 working with function argument passing
#######################
def foo(t):
    t = (1,2,3)
    return t 
    
t = (3,4,5)
foo(t)
print(t)



#############################################################################
#
# Question 1 - in recitation sheet
#
tup_a = (10, 12, 13, 14)
print(tup_a)

tup_b = ("CS1010S", "CS1231")
print(tup_b)

tup_c = tup_a + tup_b
print(tup_c)
print(14 in tup_a)
print(11 in tup_c)
tup_d = tup_b[0]*4
print(tup_d[0])
print(tup_d[1:])
count = 0
for i in tup_a:
    count = count + i
print(count)
print(max(tup_a))
print(min(tup_a))
print(max(tup_c))   # error
print(min(tup_c))


# Question 1 - own Python Tutor 

#######################
# in python tutor    #3
#######################

tmp_cc=("aa", "bab", "babb", "ab", "AA", "BB")
# use ord("a")
# use ord("A")
# see ASCII table
print(max(tmp_cc))
print(min(tmp_cc))   # use ord("A") to find the 

a = (1,2,4,5)
b = ("a", "b", "c")
c = a + b

d = a * 3  
d = (a) * 3  # this is a new d though the answer is the same
e = (a,) * 3 
a = (1,2)
print (e)

print(len(a))
print(len(d))
print(len(e))

print (1 in a)
print ("a" in a)
print (a in a)
print (a in (a))
print (a in (a,))
print (a in ((1,2),))  # also true

for ele in c:
    print (ele)

print(min(a))
print(max(a))
print(min(b))
print(max(b))
# print(min(c))  # error
# print(max(c))

# like a string
##print(c)
##print(c[1:])
##print(c[:-1])
##print(c[::-2])
##print(c[1:3])
##print(c[8]) # error
##print(c[8:])

st="abcdef"
print(st[::-1])
print(st[-1::-1])
print(st[0::-1])
print(st[:-1:-1])
print(st[:-2:-1])
#print(st[-8:])
#print(st[-8])  # error


# Question 2
# ask student to do
(1,2,3)
(1,)+(2,)+(3,)
(1,)+(2,3)
(1,2)+(3,)
(1,2,)+(3,)
(1,2,,)+(3,) # error
print( '(1, (2), 3)')  # printing of string rather than tuple

(1,(2,), 3)
(1,)+((2,),)+(3,)
((1,2), (3,4), (5,6))

#######################
# in python tutor    #4
#######################
n = (1, 2, 3)
print("length of n:", len(n))

m = (1, (2), 3)
print("length of m:", len(m))
#print("length of m[1]:", len(m[1])) # error because int has no length

p = (1, (2,), 3)
print("length of p:", len(p))
print("length of p[1]:", len(p[1]))

q = ((1, 2), (3, 4), (5, 6))
print("length of q:", len(q))
print("length of q[0]:", len(q[0]))
print("length of q[1]:", len(q[1]))
print("length of q[2]:", len(q[2]))
####################################

# Question 3
# important is the box and pointer diagram
# in python tutor #4
s = (7, 6, 5, 4, 3, 2, 1)
print(s[3])
print("length of s: ", len(s))

t = (7, (6, 5, 4), (3, 2), 1)
print(t[1][2])
print("length of t: ", len(t))
print("length of t[1]: ", len(t[1]))
print("length of t[2]: ", len(t[2]))
print("length of t[3]: ", len(t[3]))   # error

u = (7, ((6, 5, (4 ,), 3), 2), 1)
print(u[1][0][2][0])
print("length of u: ", len(u))
print("length of u[1]: ", len(u[1]))
print("length of u[1][0]: ", len(u[1][0]))
print("length of u[1][0][2]: ", len(u[1][0][2]))
print("length of u[1][0][0]: ", len(u[1][0][0]))


# Question 4
# not realistic -- suppose to be in a file processing
#
def make_units(lecture, tutorial, lab, homework, prep):
    return (lecture, tutorial, lab, homework, prep)

def make_module(course_code, units):
    return (course_code, units)

def get_module_code(course):
    return course[0]

def get_module_units(course):
    return course[1]

def get_module_total_units(units):
    return units[0] + units[1] + units[2] + units[3] + units[4]

CS1010X = make_module( "CS1010x", (3, 2, 1, 3, 3) )
MA1001 = make_module( "MA1001", (3, 2, 1, 2, 2))
MAxxx1 = make_module( "MAxxx1", (1, 1, 1, 2, 2))

# (a)
# time: O(1),    space: O(1)
def make_empty_schedule():
    return ()

# (b)ver 1
# time: O(n),   space: O(n)....n is the number of courses
def add_class(course, schedule):
    if (course in schedule):
        return schedule
    else:
        return (course, ) + schedule  # becareful of the "," after "course"

# (b) ver 2   -- recursion version
# time: O(n^2),  space: O(n^2)
def add_class(course, schedule):
    if schedule == ():
        return (course, )
    elif course == schedule[0]: # means course already existed
        return schedule
    else:
        return (schedule[0],) + add_class(course, schedule[1:])

schedule_tan = make_empty_schedule()
schedule_tan = add_class( CS1010X, schedule_tan)
schedule_tan = add_class( MA1001, schedule_tan )
#MA1001 = make_module( "MXXXX", (1, 1, 1, 2, 2))

# (c)
# time: O(n),   space: O(1)
def get_units(course):
    return get_module_total_units(get_module_units(course))

def total_scheduled_units(schedule):
    total = 0
    for course in schedule:
        total = total + get_units(course)
    return total11

print(total_scheduled_units( schedule_tan ))

# (d) version 0:
def drop_class(schedule, course):
    if course not in schedule:
        return schedule
    
    i = schedule.index(course)
    return schedule[:i] + schedule[i+1:]


# (d) version 1:
# time: O(n^2),  space: O(n^2)
def drop_class(schedule, course):
    if schedule == ():
        return schedule
    elif schedule[0] == course:
        return drop_class(schedule[1:], course)
    else:
        return (schedule[0],) + drop_class(schedule[1:], course)
    
# T(n) = O(1) + O(1) + O(1_ + O(n) + T(n-1) + O(n)

# (d) version 2:
# time: O(n^2),   space: O(n)
def drop_class(schedule, course):
    new_schedule = make_empty_schedule()   # no choice but to do this way
    for item in schedule:
        if item == course:
            continue
        else:
            new_schedule += (item,)
    return new_schedule

# (e)
# time: O(n^2),   ( space: O(n) )  
def credit_limit(schedule, max_credits):
    total = total_scheduled_units(schedule) # O(n)
    while (total > max_credits):
        total -= get_units(schedule[0])
        schedule = schedule[1:]
    return schedule








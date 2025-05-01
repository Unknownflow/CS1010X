############################################################
#
# Question 1
#
#############################################################
def day_of_date( dd, mm, yyyy ):
    def is_leap_year(yyyy):
        if yyyy % 400 == 0:
            return True
        elif yyyy % 100 != 0:
            return False
        elif yyyy % 4 == 0:
            return True
        else:
            return False
    
    days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    box_1 = dd
    if is_leap_year(yyyy):
        box_2 = {1: 6, 2: 2, 3: 3, 4: 6, 5: 1, 6: 4, 7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5}
    else:
        box_2 = {1: 0, 2: 3, 3: 3, 4: 6, 5: 1, 6: 4, 7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5}
    box_3 = {15: 0, 16: 6, 17: 4, 18: 2, 19: 0, 20: 6}
    yyyy_str = str(yyyy)
    box_4 = int(yyyy_str[2:])
    box_5 = box_4 // 4
    century = yyyy // 100
    total = box_1 + box_2[mm] + box_3[century] + box_4 + box_5

    return days[total % 7]



print ("")
print (" * * * Question 1 * * *")
print (day_of_date(25, 12, 2000) == "Monday")
print (day_of_date(25, 12, 1900) == "Tuesday")
print (day_of_date(1, 1, 1997) == "Wednesday")
print (day_of_date(11, 11, 1999) == "Thursday")
print (day_of_date(1, 1, 1897) == "Friday")
print (day_of_date(5, 6, 2021) == "Saturday")
print (day_of_date(5, 6, 1898) == "Sunday")

############################################################
#
# Question 2
#
#############################################################
from runes import *

def stackn(n,pic):
    if n == 1: 
        return pic
    else: 
        return stack_frac(1/n, pic, stackn(n-1, pic))

def nxn(n,pic):
    return stackn(n, quarter_turn_right(stackn(n, quarter_turn_left(pic) ) ) )

print ("")
print (" * * * Question 2 * * *")
#########
#
# Question 2: Question 2 A.
#
#########
def stackn_alt(n, pic1, pic2):
    if n == 1: 
        return pic1
    else: 
        return stack_frac(1/n, pic1, stackn_alt(n-1, pic2, pic1))
    
#show(stackn_alt(5, make_cross(nova_bb), make_cross(rcross_bb)))
#show(stackn_alt(6, make_cross(nova_bb), make_cross(rcross_bb)))
#show(stackn_alt(5, make_cross(circle_bb), make_cross(heart_bb)))

#########
#
# Question 3: Question 2 B. 
# Recursive
#
#########
def nxn_alt(n, pic1, pic2):
    if n % 2 != 0:
        return stackn_alt(n,
            quarter_turn_right(stackn_alt(n, pic1, pic2)),
            quarter_turn_right(stackn_alt(n, pic2, pic1))
        )
    else:
        return stackn_alt(n,
            quarter_turn_right(stackn_alt(n, pic2, pic1)),
            quarter_turn_right(stackn_alt(n, pic1, pic2))
        )
    
#show(nxn_alt(5, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(4, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(6, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(5, make_cross(circle_bb), make_cross(heart_bb)))

#########
#
# Question 4: Question 2 C. 
# Use for or while loop
#
#########
def nxn_alt(n,pic1, pic2):
    row1 = pic1
    for i in range(n):
        if i % 2 == 0: 
            row1 = stack_frac(i/(i+1), row1, pic1)
        else:
            row1 = stack_frac(i/(i+1), row1, pic2)

    row2 = pic1
    for i in range(n):
        if i % 2 == 0: 
            row2 = stack_frac(i/(i+1), row2, pic2)
        else:
            row2 = stack_frac(i/(i+1), row2, pic1)

    row1 = quarter_turn_right(row1)
    row2 = quarter_turn_right(row2)
    res = row1

    if n % 2 != 0:
        for i in range(n):
            if i % 2 == 0:
                res = stack_frac(i/(i+1), res, row1)
            else:
                res = stack_frac(i/(i+1), res, row2)
    else:
        for i in range(n):
            if i % 2 == 0:
                res = stack_frac(i/(i+1), res, row2)
            else:
                res = stack_frac(i/(i+1), res, row1)
                      
    return res

#show(nxn_alt(5, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(4, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(6, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(5, make_cross(circle_bb), make_cross(heart_bb)))


############################################################
#
# Question 3
#
#############################################################
lst = [ [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 0, 1, 2, 3, 4, 5, 6],
        [7, 8, 9, 0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9, 0, 1, 2],
        [3, 4, 5, 6, 7, 8, 9, 0] ]

lst2 = [[-2, 94, 7, -90, -34],
        [30, 24, 3, 100, -23],
        [22, -9, 49, -45, 29], 
        [-65, -28, -65, 93, -76], 
        [58, -36, 36, 80, 54]]

lst3 = [[-66, 45, 95, -84, -35, -70, 26, 94, 15, 20],
        [66, -3, -47, -76, 24, -93, -1, 10, 55, 95], 
        [96, -100, 78, 14, -32, 84, -42, 51, -74, -19], 
        [-93, -95, -94, 66, 38, -98, -3, 75, -45, 8], 
        [85, -93, 35, -44, 95, 12, 26, 41, -41, -12]]

lst4 = [[-86, -77, -79, -8, -57],
        [88, 71, -22, -36, 55],
        [-46, 55, -91, 48, 74],
        [-60, 10, 63, 0, 85],
        [30, -5, 39, 13, 28],
        [-32, -91, -93, -7, 19],
        [-19, -3, 8, 34, -58],
        [43, -55, -40, -41, -94],
        [-55, -17, -56, -66, 30],
        [30, -8, 31, 72, 43]]


def rect_sum(lst, i, j):
    sum = 0
    for ii in range(0, i+1):
        for jj in range(0, j+1):
            sum += lst[ii][jj]
    return sum

def naive_sum(lst):
    result_lst = []
    for i in range(0, len(lst)):
        result_lst.append([0]*len(lst[0]))
        for j in range(0, len(lst[0])):
            result_lst[i][j] = rect_sum(lst, i, j)
    return result_lst

sample_result = naive_sum(lst)
sample_result2 = naive_sum(lst2)
sample_result3 = naive_sum(lst3)
sample_result4 = naive_sum(lst4)

#########
#
# Question 5: Question 3 A.
#
#########
# State the time complexity in coursemology
# O(n^2 * m^2)

#########
#
# Question 6: Question 3 B.
#
#########
def better_sum(lst):
    result_lst = []

    # copying lst to result_lst
    for i in range(0, len(lst)):
        result_lst.append([])
        for j in range(0, len(lst[0])):
            result_lst[i].append(lst[i][j])

    # prefix sum for rows
    for i in range(len(lst)):
        for j in range(1, len(lst[0])):
            result_lst[i][j] = result_lst[i][j] + result_lst[i][j-1]

    # prefix sum for cols
    for j in range(len(lst[0])):
        for i in range(1, len(lst)):
            result_lst[i][j] = result_lst[i-1][j] + result_lst[i][j]


    return result_lst


print ("")
print (" * * * Question 3B * * *")
print( sample_result == better_sum(lst) )
print( sample_result2 == better_sum(lst2) )
print( sample_result3 == better_sum(lst3) )
print( sample_result4 == better_sum(lst4) )

#########
#
# Question 7: Question 3 C.
#
#########
def dp_sum(lst):
    result_lst = []

    # copying lst to result_lst
    for i in range(0, len(lst)):
        result_lst.append([])
        for j in range(0, len(lst[0])):
            result_lst[i].append(lst[i][j])

    for i in range(1, len(lst)):
        result_lst[i][0] += result_lst[i-1][0]
    
    for j in range(1, len(lst[0])):
        result_lst[0][j] += result_lst[0][j-1]
    
    for i in range(1, len(lst)):
        for j in range(1, len(lst[0])):
            result_lst[i][j] = result_lst[i][j] + result_lst[i-1][j] + result_lst[i][j-1] - result_lst[i-1][j-1]

    return result_lst
            
            

print ("")
print (" * * * Question 3C * * *")
print( sample_result == dp_sum(lst) )
print( sample_result2 == dp_sum(lst2) )
print( sample_result3 == dp_sum(lst3) )
print( sample_result4 == dp_sum(lst4) )

#########
#
# Question 8: Question 3 D.
#
#########
# State the time complexity in coursemology
# O(mn) for both
#########
#
# Question 9: Question 3 E.
#
#########
def search_rect_sum(result_lst, ii, jj, i, j):
    if ii == 0:
        col_sum = 0
    else:
        col_sum = result_lst[ii-1][j]
    
    if jj == 0:
        row_sum = 0
    else:
        row_sum = result_lst[i][jj-1]
      
    if ii == 0 or jj == 0:
        left_corner = 0
    else:
        left_corner = result_lst[ii-1][jj-1]
    
    return result_lst[i][j] - row_sum - col_sum + left_corner
    
print ("")
print (" * * * Question 3E * * *")
x = sample_result
print( search_rect_sum(x, 0, 0, 4,7) == 180 )
print( search_rect_sum(x, 3, 6, 4,7) == 12 )
print( search_rect_sum(x, 3, 7, 4,7) == 2)
print( search_rect_sum(x, 4, 6, 4,7) == 9)
print( search_rect_sum(x, 1, 0, 4, 7) == 144)
print( search_rect_sum(x, 1, 0, 3, 6) == 90)
print( search_rect_sum(x, 0, 1, 3, 6) == 96)
print( search_rect_sum(x, 1, 1, 3, 6) == 69)
print( search_rect_sum(x, 2, 3, 3, 6) == 24)

print( search_rect_sum(sample_result2, 0, 0, 4, 4) == 206 )
print( search_rect_sum(sample_result3, 2, 3, 4, 9) == 100 )
print( search_rect_sum(sample_result4, 3, 2, 9, 4) == 10 )

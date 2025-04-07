#
# CS1010X --- Programming Methodology
#
# Sidequest 9.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json
import time

#####################
# Reading json file #
#####################

def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google it :P

    For example, file.txt contains:
    [["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"], ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"], ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]]

    Calling read_json('file.txt') will return the following array
    [
        ["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"],
        ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"],
        ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]
    ]
    """
    datafile = open(filename, 'r', encoding='utf-8')
    return json.loads(datafile.read())

#############
# Accessors #
#############

def module_code(module):
    return module[0]

def module_name(module):
    return module[1]

def module_prof(module):
    return module[2]


###########
# Task 1a #
###########

def merge_lists(all_lst):
    # Your code here
    result = []
    all_lst = list(filter(lambda lst: len(lst) > 0, all_lst))
            
    while len(all_lst) > 0:
        smallest_num = all_lst[0][0]
        smallest_idx = 0
        for i in range(1, len(all_lst)):
            # find the smallest num and idx in the lists
            if len(all_lst[i]) > 0 and all_lst[i][0] < smallest_num:
                smallest_num = all_lst[i][0]
                smallest_idx = i
        
        # append smallest num to result and remove the num from the lst
        result.append(smallest_num)
        all_lst[smallest_idx].pop(0)

        # if empty list after item is popped, remove the lst
        if len(all_lst[smallest_idx]) == 0: 
            all_lst.pop(smallest_idx)

    return result

all_lst = [[2, 7, 10], [0, 4, 6], [3, 11]]
# print("## Q1a ##")
# print(merge_lists(all_lst)) # [0, 2, 3, 4, 6, 7, 10, 11]
# print(merge_lists([[2,3,4], [], [1,5]])) 

###########
# Task 1b #
###########

def merge(lists, field):
    # Your code here
    result = []
    lists = list(filter(lambda lst: len(lst) > 0, lists))
            
    while len(lists) > 0:
        smallest_item = field(lists[0][0])
        smallest_idx = 0
        for i in range(1, len(lists)): # time: O(n)
            # find the smallest item and idx in the lists
            field_item = field(lists[i][0])
            if len(lists[i]) > 0 and field_item < smallest_item:
                smallest_item = field_item
                smallest_idx = i
        
        # append courses to result and remove the course from the lst
        result.append(lists[smallest_idx][0])
        lists[smallest_idx].pop(0)

        # if empty list after item is popped, remove the lst
        if len(lists[smallest_idx]) == 0: 
            lists.pop(smallest_idx)

    return result


list_of_lists = [[["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"],
                  ["CS3235", "COMPUTER SECURITY", "NORMAN HUGH ANDERSON"]],
                 [["CS4221", "DATABASE DESIGN", "LING TOK WANG"],
                  ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"]]]
# print("## Q1b ##")
# print(merge(list_of_lists, module_prof))
# [[’CS1010S’, ’PROGRAMMING METHODOLOGY’, ’LEONG WING LUP, BEN’],
#  [’CS4221’, ’DATABASE DESIGN’, ’LING TOK WANG’],
#  [’CS3235’, ’COMPUTER SECURITY’, ’NORMAN HUGH ANDERSON’],
#  [’CS2010’, ’DATA STRUCTURES & ALGORITHMS II’, ’STEVEN HALIM’]

##########
# Task 2 #
##########

test = [["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"], ["CS3241", "COMPUTER GRAPHICS", "CHENG HOLUN"], ["CS4243", "COMPUTER VISION AND PATTERN RECOGNITION", "NG TECK KHIM"], ["CS4345", "GENERAL PURPOSE COMPUTATION ON GPU", "LOW KOK LIM"], ["CS3235", "COMPUTER SECURITY", "NORMAN HUGH ANDERSON"], ["BT1101", "INTRODUCTION TO BUSINESS ANALYTICS", "KIM SEUNG HYUN"], ["MA1101R", "LINEAR ALGEBRA I", "NG KAH LOON"], ["CS3230", "DESIGN AND ANALYSIS OF ALGORITHMS", "RAHUL JAIN"], ["MA1100", "FUNDAMENTAL CONCEPTS OF MATHEMATICS", "VICTOR TAN"], ["ST2334", "PROBABILITY AND STATISTICS", "JASRA, AJAY"], ["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"], ["CS3244", "MACHINE LEARNING", "TAN CHEW LIM"], ["CS5321", "NETWORK SECURITY AND MANAGEMENT", "CHANG EE-CHIEN"], ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"]]

def merge_sort(lst, k, field):
    # Your code here    
    def split_lst(lst, k):
        # list will become a List[List[Modules]]
        if k == 0:
            return []
        if k == 1:
            return [lst]
        split_pt = len(lst) // k

        return [lst[:split_pt]] + split_lst(lst[split_pt:], k-1) # time and space: O(k)
    
    if len(lst) <= 1:
        return lst
    else: 
        sub_lists = split_lst(lst, k) # divide lst to k sub lists, time: O(k)
        for i in range(len(sub_lists)): # time: O(k)
            sub_sub_list = split_lst(sub_lists[i], len(sub_lists[i])) # make the sublist into list of size 1, time: O(n/k)
            sub_lists[i] = merge(sub_sub_list, field) # merge back the sub sub list, time, space: O(nlogk)

        result = merge(sub_lists, field) # merge back sublist
        return result
    

# (merge_sort(test, 7, module_code))
# For your own debugging
# print("### Q2 ###")
modules = read_json('./sidequest09.1/modules_small.txt')
for module in merge_sort(modules, 2, module_code):
   print(module)


########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########

def print_list_to_str(list):
    return '\n'.join(str(x) for x in list)

def test(testfile_prefix):
    print("\n*** Testing with ",testfile_prefix,".txt ***")
    modules = read_json(testfile_prefix+'.txt')
    total_time = 0

    # Open correct answers
    modules_sorted_code = open(testfile_prefix+'_sorted_code.txt', 'r', encoding='utf-8').read()
    modules_sorted_name = open(testfile_prefix+'_sorted_name.txt', 'r', encoding='utf-8').read()
    modules_sorted_prof = open(testfile_prefix+'_sorted_prof.txt', 'r', encoding='utf-8').read()

    ks = [2,3,5,8,13,21,34,55,89,144]
    pass_k = 0

    for k in ks:
        start_time = time.time()
        # Execute
        modules_answer_code = merge_sort(modules, k, module_code)
        modules_answer_name = merge_sort(modules, k, module_name)
        modules_answer_prof = merge_sort(modules, k, module_prof)
        end_time = time.time()
        total_time += (end_time - start_time)

        # Check
        code_same = print_list_to_str(modules_answer_code) == modules_sorted_code
        name_same = print_list_to_str(modules_answer_name) == modules_sorted_name
        prof_same = print_list_to_str(modules_answer_prof) == modules_sorted_prof
        if (code_same and name_same and prof_same):
            pass_k += 1
        print("k = ", k, ", code: ",code_same,", name: ", name_same,", prof: ",prof_same)

    print(pass_k,"/", len(ks), " correct! Total time taken: ", total_time, " seconds.")

print("## Q2 ##")
# test('./sidequest09.1/modules_small')
# test('./sidequest09.1/modules')
# test('./sidequest09.1/modules_empty')

# time complexity of merge : O(n), space compelxity also O(n)
# time complexity of split_lst : O(k), space complexity also O(k)
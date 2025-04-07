#
# CS1010S --- Programming Methodology
#
# Mission 8 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from ippt import *
import csv

##########
# Task 1 #
##########

# Function read_csv has been given to help you read the csv file.
# The function returns a tuple of tuples containing rows in the csv
# file and its entries.

# Alternatively, you may use your own method.

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

def read_data(filename):
    rows = read_csv(filename)

    data = tuple()
    rep_title = map(lambda rep: int(rep), rows[0][1:])
    age_title = tuple()

    # data format: age, data1, data2, data3...
    for row in rows[1:]:
        age_title += (int(row[0]), )
        data += (map(lambda data_part: int(data_part), row[1:]),)
        
    return create_table(data, age_title, rep_title)

pushup_table = read_data("pushup.csv")
situp_table = read_data("situp.csv")
run_table = read_data("run.csv")

ippt_table = make_ippt_table(pushup_table, situp_table, run_table)

print("## Q1 ##")
# Sit-up score of a 24-year-old who did 10 sit-ups.
print(access_cell(situp_table, 24, 10))    # 0

# Push-up score of a 18-year-old who did 30 push-ups.
# print(access_cell(pushup_table, 18, 30))   # 16

# Run score of a 30-year old-who ran 12 minutes (720 seconds)
# print(access_cell(run_table, 30, 720))     # 36

# Since our run.csv file does not have data for 725 seconds, we should
# get None if we try to access that cell.
# print(access_cell(run_table, 30, 725))     # None


##########
# Task 2 #
##########

import math
def pushup_score(pushup_table, age, pushup):
    if pushup > 60:
        return access_cell(pushup_table, age, 60)
    elif pushup == 0:
        return 0
    else:
        return access_cell(pushup_table, age, pushup)

def situp_score(situp_table, age, situp):
    if situp > 60:
        return access_cell(situp_table, age, 60)
    elif situp == 0:
        return 0
    else:
        return access_cell(situp_table, age, situp)

def run_score(run_table, age, run):
    if run > 1100:
        return access_cell(run_table, age, 1100)
    elif run < 510:
        return access_cell(run_table, age, 510)
    else:
        # round up to nearest 10
        run_time = math.ceil(run/10) * 10
        return access_cell(run_table, age, run_time)

# print("## Q2 ##")
# print(pushup_score(pushup_table, 18, 61))   # 25
# print(pushup_score(pushup_table, 18, 70))   # 25
# print(situp_score(situp_table, 24, 0))      # 0

# print(run_score(run_table, 30, 720))        # 36
# print(run_score(run_table, 30, 725))        # 35
# print(run_score(run_table, 30, 735))        # 35
# print(run_score(run_table, 30, 500))        # 50
# print(run_score(run_table, 30, 1300))       # 0


##########
# Task 3 #
##########

def ippt_award(score):
    if score < 51:
        return "F"
    elif score < 61:
        return "P"
    elif score < 75:
        return "P$"
    elif score < 85:
        return "S"
    else:
        return "G"

# print("## Q3 ##")
# print(ippt_award(50))     # F
# print(ippt_award(51))     # P
# print(ippt_award(61))     # P$
# print(ippt_award(75))     # S
# print(ippt_award(85))     # G


##########
# Task 4 #
##########

def ippt_results(ippt_table, age, pushup, situp, run):
    # retrieve tables
    pushup_table = get_pushup_table(ippt_table)
    situp_table = get_situp_table(ippt_table)
    run_table = get_run_table(ippt_table)

    # retrieve scores
    pushup_scores = int(pushup_score(pushup_table, age, pushup))
    situp_scores = int(situp_score(situp_table, age, situp))
    run_scores = int(run_score(run_table, age, run))

    # sum scores and get award
    score = pushup_scores + situp_scores + run_scores
    award = ippt_award(score)
    return (score, award)

# print("## Q4 ##")
# print(ippt_results(ippt_table, 25, 30, 25, 820))      # (53, 'P')
# print(ippt_results(ippt_table, 28, 56, 60, 530))      # (99, 'G')
# print(ippt_results(ippt_table, 38, 18, 16, 950))      # (36, 'F')
# print(ippt_results(ippt_table, 25, 34, 35, 817))      # (61, 'P$')
# print(ippt_results(ippt_table, 60, 70, 65, 450))      # (100, 'G')


##########
# Task 5 #
##########
def make_training_program(rate_pushup, rate_situp, rate_run):
    def training_program(ippt_table, age, pushup, situp, run, days):
        new_pushups = pushup + days // rate_pushup
        new_situps = situp + days // rate_situp
        new_run = run - days // rate_run
        ippt_result = ippt_results(ippt_table, age, new_pushups, new_situps, new_run)

        return (new_pushups, new_situps, new_run, ippt_result)

    return training_program

# print("## Q5 ##")
tp = make_training_program(7, 3, 10)
# print(tp(ippt_table, 25, 30, 25, 820, 30))        # (34, 35, 817, (61, 'P$'))


##########
# Bonus  #
##########

def make_tp_bonus(rate_pushup, rate_situp, rate_run): 
    max_pushups = 60
    max_situps = 60
    min_run = 510

    def tp_bonus(ippt_table, age, pushup, situp, run, days):

        ippt_score, award = ippt_results(ippt_table, age, pushup, situp, run)
        if ippt_score == 100:
            return (pushup, situp, run, (ippt_score, award))

        while days > 0:
            pushups_needed = 1
            situps_needed = 1
            seconds_needed = 1
            ippt_score = ippt_results(ippt_table, age, pushup, situp, run)[0]

            while True:
                # find the number of pushups needed to get to the next point
                new_pushups = pushup + pushups_needed
                new_score = ippt_results(ippt_table, age, new_pushups, situp, run)[0]

                if new_pushups > max_pushups:
                    pushups_needed = -1
                    break
                if new_score != ippt_score:
                    break

                pushups_needed += 1
            
            while True:
                # find the number of situps needed to get to the next point
                new_situps = situp + situps_needed
                new_score = ippt_results(ippt_table, age, pushup, new_situps, run)[0]

                if new_situps > max_situps:
                    situps_needed = -1
                    break
                if new_score != ippt_score:
                    break

                situps_needed += 1

            while True:
                # find the number of seconds needed to get to the next point
                new_run = run - seconds_needed
                new_score = ippt_results(ippt_table, age, pushup, situp, new_run)[0]
                
                if new_run < min_run:
                    seconds_needed = -1
                    break
                if new_score != ippt_score:
                    break

                seconds_needed += 1
            
            # calculate days needed to get 1 more pt for each training
            pushup_days_needed = pushups_needed * rate_pushup
            situp_days_needed = situps_needed * rate_situp
            run_days_needed = seconds_needed * rate_run

            min_days = 100000000000000000000000000000000000000000000000
            if pushup_days_needed > 0 and pushup_days_needed < min_days:
                min_days = pushup_days_needed
            
            if situp_days_needed > 0 and situp_days_needed < min_days:
                min_days = situp_days_needed
              
            if run_days_needed > 0 and run_days_needed < min_days:
                min_days = run_days_needed

            if min_days == 100000000000000000000000000000000000000000000000:
                continue
            
            days -= min_days

            if days < 0:
                continue
            
            if pushup_days_needed == min_days:
                pushup += pushups_needed
            elif situp_days_needed == min_days:
                situp += situps_needed
            elif run_days_needed == min_days:
                run -= seconds_needed
        
        result = ippt_results(ippt_table, age, pushup, situp, run)
        return (pushup, situp, run, result)

    return tp_bonus

tp_bonus = make_tp_bonus(7, 3, 10)

# Note: Depending on your implementation, you might get a different number of
# sit-up, push-up, and 2.4km run timing. However, the IPPT score and grade
# should be the same as the sample output.

print(tp_bonus(ippt_table, 25, 20, 30, 800, 30))      # (20, 40, 800, (58, 'P'))
print(tp_bonus(ippt_table, 25, 20, 30, 800, 2))       # (20, 30, 800, (52, 'P'))

print(ippt_results(ippt_table, 25, 20, 40, 800))
print(ippt_results(ippt_table, 25, 20, 31, 800))
print('fast', tp_bonus(ippt_table, 25, 60, 60, 500, 200))
print('fast', tp_bonus(ippt_table, 25, 60, 60, 1000, 200))
print('sohai', tp_bonus(ippt_table, 25, 0, 0, 2000, 400))
print(ippt_results(ippt_table, 25, 31, 60, 2000))
print('wtf', tp_bonus(ippt_table, 25, 20, 30, 800, 50)[3]) # (61, 'P$)




# tp_bonus = make_tp_bonus(600, 600, 1)
# print(tp_bonus(ippt_table, 25, 20, 30, 800, 20))      # (20, 40, 800, (58, 'P'))

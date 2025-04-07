# CS1010S --- Programming Methodology
#
# Mission 7 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import datetime
import csv

###############
# Pre-defined #
###############

def map(fn, seq):
    res = ()

    for ele in seq:
        res = res + (fn(ele), )
    return res

def filter(pred, seq):
    res = ()

    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res

###############
# Station ADT #
###############

def make_station(station_code, station_name):
    return (station_code, station_name)

def get_station_code(station):
    return station[0]

def get_station_name(station):
    return station[1]

test_station1 = make_station('CC2', 'Bras Basah')
test_station2 = make_station('CC3', 'Esplanade')
test_station3 = make_station('CC4', 'Promenade')


############
## Task 1 ##
############

def make_train(train_code):
    ''' Do NOT modify this function'''
    return (train_code,)

test_train = make_train('TRAIN 0-0')
#############
# Task 1a   #
#############

def get_train_code(train):
    return train[0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1A
print("## Task 1a ##")
print(get_train_code(test_train))

# Expected Output #
# TRAIN 0-0

#############
# Task 1b   #
#############

def make_line(name, stations):
    return (name, stations)

def get_line_name(line):
    return line[0]

def get_line_stations(line):
    return line[1]

def get_station_by_name(line, station_name):
    stations = get_line_stations(line)

    for station in stations:
        if get_station_name(station) == station_name:
            return station
      
    return None

def get_station_by_code(line, station_code):
    stations = get_line_stations(line)

    for station in stations:
        if get_station_code(station) == station_code:
            return station
      
    return None

def get_station_position(line, station_code):
    stations = get_line_stations(line)

    for i in range(len(stations)):
        if station_code == get_station_code(stations[i]):
            return i
    
    return -1

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1B
print("## Task 1b ##")
test_line = make_line('Circle Line', (test_station1, test_station2, test_station3))
print(get_line_name(test_line))
print(get_line_stations(test_line))
print(get_station_by_name(test_line, 'Bras Basah'))
print(get_station_by_code(test_line, 'CC4'))
print(get_station_by_name(test_line, 'Toa Payoh'))
print(get_station_by_code(test_line, 'CC1'))
print(get_station_position(test_line, 'CC2'))
print(get_station_position(test_line, 'CC5'))

# Expected Output #
# Circle Line
# (('CC2', 'Bras Basah'), ('CC3', 'Esplanade'), ('CC4', 'Promenade'))
# ('CC2', 'Bras Basah')
# ('CC4', 'Promenade')

#############
# Task 1c   #
#############

def make_train_position(is_moving, from_station, to_station):
    ''' Do NOT modify this function'''
    return (is_moving, from_station, to_station)

def get_is_moving(train_position):
    return train_position[0]

def get_direction(line, train_position):
    from_station_code = get_station_code(train_position[1])
    to_station_code = get_station_code(train_position[2])
    from_position = get_station_position(line, from_station_code)
    to_position = get_station_position(line, to_station_code)

    if from_position < to_position: # ascending order
        return 0
    else: # otherwise descending order
        return 1
    

def get_stopped_station(train_position):
    if get_is_moving(train_position): # stationary train, return None
        return None
    
    return train_position[1]

def get_previous_station(train_position):
    if not get_is_moving(train_position): # train not moving, return None
        return None
    
    return train_position[1]

def get_next_station(train_position):
    return train_position[2]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1C
# print("## Task 1c ##")
test_train_position1 = make_train_position(False, test_station1, test_station2)
test_train_position2 = make_train_position(True, test_station3, test_station2)
# # print(get_is_moving(test_train_position1))
# print(get_is_moving(test_train_position2))

# print(get_direction(test_line, test_train_position1))
# # print(get_direction(test_line, test_train_position2))

# print(get_stopped_station(test_train_position1))
# print(get_stopped_station(test_train_position2))

# print(get_previous_station(test_train_position1))
# print(get_previous_station(test_train_position2))

# # print(get_next_station(test_train_position1))
# print(get_next_station(test_train_position2))


# Expected Output #
# True
# 0
# ('CC2', 'Bras Basah')
# ('CC4', 'Promenade')
# ('CC3', 'Esplanade')

#############
# Task 1d   #
#############

def make_schedule_event(train, train_position, time):
    return (train, train_position, time)

def get_train(schedule_event):
    return schedule_event[0]

def get_train_position(schedule_event):
    return schedule_event[1]

def get_schedule_time(schedule_event):
    return schedule_event[2]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1D
# print("## Task 1d ##")
test_bd_event1 = make_schedule_event(test_train, test_train_position2, datetime.datetime(2016, 1, 1, 9, 27))
test_bd_event2 = make_schedule_event(test_train, test_train_position1, datetime.datetime(2016, 1, 1, 2, 25))
# print(get_train(test_bd_event1))
# print(get_train_position(test_bd_event1))
# print(get_schedule_time(test_bd_event1))

# print(get_train(test_bd_event2))
# print(get_train_position(test_bd_event2))
# print(get_schedule_time(test_bd_event2))

# Expected Output #
# ('TRAIN 0-0',)
# (True, ('CC4', 'Promenade'), ('CC3', 'Esplanade'))
# 2016-01-01 09:27:00


############
## Task 2 ##
############

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

#############
# Task 2a   #
#############

def parse_lines(data_file):
    rows = read_csv(data_file)[1:]
    lines = ()
    curr_line_name = rows[0][2]

    curr_line_stations = ()
    for row in rows:
        code, station_name, line_name = row
        if line_name == curr_line_name:
            # Addition #1
            station = make_station(code, station_name)
            curr_line_stations = curr_line_stations + (station,)
        else:
            # Addition #2
            line = make_line(curr_line_name, curr_line_stations)
            lines = lines + (line, )
            curr_line_name = line_name
            station = make_station(code, station_name)
            curr_line_stations = (station,)

    # Addition #3
    line = make_line(line_name, curr_line_stations)
    lines = lines + (line, )

    return lines

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2A. THIS IS NOT OPTIONAL TESTING!
LINES = parse_lines('station_info.csv')

# for line in LINES:
#     print()
#     print(line)
#     print('line',get_line_name(line))

CCL = filter(lambda line: get_line_name(line) == 'Circle Line', LINES)[0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2A
# print("## Task 2a ##")
# print(get_line_stations(CCL)[5:8])

# Expected Output #
# (('CC6', 'Stadium'), ('CC7', 'Mountbatten'), ('CC8', 'Dakota'))

#############
# Task 2b   #
#############

def parse_events_in_line(data_file, line):
    rows = read_csv(data_file)[1:]
    events = ()
    
    for row in rows:
        train_code, is_moving, from_code, to_code, date, time = row
        train = make_train(train_code)
        from_station = get_station_by_code(line, from_code)
        to_station = get_station_by_code(line, to_code)
        
        if is_moving == "False":
            is_moving = False
        else:
            is_moving = True

        # formatting the date and time to be the correct type
        day, month, year = map(lambda x: int(x), date.split('/'))
        hour, minute = map(lambda x: int(x), time.split(":"))
        datetime_obj = datetime.datetime(year, month, day, hour, minute)

        train_position = make_train_position(
            is_moving, 
            from_station, 
            to_station
            )
        schedule_event = make_schedule_event(
            train, 
            train_position, 
            datetime_obj
            ) 
        events = events + (schedule_event, )

    return events

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2B. THIS IS NOT OPTIONAL TESTING!
BD_EVENTS = parse_events_in_line('breakdown_events.csv', CCL)

# print(BD_EVENTS)
# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2B
print("## Task 2b ##")
print(BD_EVENTS[9])
print((('TRAIN 1-11',), (False, ('CC23', 'one-north'), ('CC22', 'Buona Vista')), datetime.datetime(2017, 1, 6, 7, 9)))
print(BD_EVENTS[27])

# Expected Output #
# (('TRAIN 1-11',), (False, ('CC23', 'one-north'), ('CC22', 'Buona Vista')), datetime.datetime(2017, 1, 6, 7, 9))

############
## Task 3 ##
############

#############
# Task 3a   #
#############

def is_valid_event_in_line(bd_event, line):
    operating_hours_start = datetime.time(7, 0, 0)
    operating_hours_end = datetime.time(23, 0, 0)
    schedule_time = get_schedule_time(bd_event).time()
    train_position = get_train_position(bd_event)
    to_station = get_next_station(train_position)
    direction = get_direction(line, train_position)

    if get_is_moving(train_position): 
        # train is moving, get prev station
        from_station = get_previous_station(train_position)
    else: 
        # train is not moving, get stopped station
        from_station = get_stopped_station(train_position)
    
    # calculate diff in position of the stations
    from_pos = get_station_position(line, get_station_code(from_station))
    to_pos = get_station_position(line, get_station_code(to_station))
    diff = to_pos - from_pos
    
    if direction == 0: 
        # ascending order, hence diff shld be 1, otherwise invalid
        if diff != 1:
            return False
    else: 
        # descending oredr, hence diff shld be -1, otherwise invalid
        if diff != -1:
            return False
        
    # event earlier than 7am are not allowed
    if schedule_time < operating_hours_start:
        return False
    
    # event later than 11pm are not allowed
    if schedule_time > operating_hours_end:
        return False
    
    return True


def get_valid_events_in_line(bd_events, line):
    ''' Do NOT modify this function'''
    return filter(lambda ev: is_valid_event_in_line(ev, line), bd_events)

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 3A. THIS IS NOT OPTIONAL TESTING!
VALID_BD_EVENTS = get_valid_events_in_line(BD_EVENTS, CCL)
# print(VALID_BD_EVENTS)

# for event in VALID_BD_EVENTS:
#     print(event)

# print(len(VALID_BD_EVENTS))

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3A
# print("## Task 3a ##")
# print(is_valid_event_in_line(test_bd_event1, CCL))
# print(is_valid_event_in_line(test_bd_event2, CCL))

# Expected Output #
# True
# False

#############
# Task 3b   #
#############

def get_location_id_in_line(bd_event, line):
    train_position = get_train_position(bd_event)
    
    if not get_is_moving(train_position):
        # if train is stationary, location ID corresponds to station which train
        # is stopped at
        stopped_station = get_stopped_station(train_position)
        stopped_station_code = get_station_code(stopped_station)
        location_id = get_station_position(line, stopped_station_code)

        return location_id
    else:
        # else location id will be denoted as (0.5 + lower of the 2 station numbers)
        prev_station = get_previous_station(train_position)
        next_station = get_next_station(train_position)

        prev_station_code = get_station_code(prev_station)
        next_station_code = get_station_code(next_station)

        prev_station_pos = get_station_position(line, prev_station_code)
        next_station_pos = get_station_position(line, next_station_code)
        
        return min(prev_station_pos, next_station_pos) + 0.5

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3B
# print("## Task 3b ##")
test_loc_id1 = get_location_id_in_line(test_bd_event1, CCL)
test_loc_id2 = get_location_id_in_line(test_bd_event2, CCL)
# print(test_loc_id1)
# print(test_loc_id2)

# Expected Output #
# 2.5
# 1

############
## Task 4 ##
############

# UNCOMMENT the following to read the entire train schedule
FULL_SCHEDULE = parse_events_in_line('train_schedule.csv', CCL)    # this will take some time to run

#############
# Task 4a   #
#############

def get_schedules_at_time(train_schedule, time):
    return filter(
        lambda scheduleEvent: get_schedule_time(scheduleEvent) == time, 
        train_schedule
        )

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4A
# print("## Task 4a ##")
test_datetime = datetime.datetime(2017, 1, 6, 6, 0)
test_schedules_at_time = get_schedules_at_time(FULL_SCHEDULE[:5], test_datetime)
# print(test_schedules_at_time[1])

# Expected Output #
# (('TRAIN 1-0',), (False, ('CC29', 'HarbourFront'), ('CC28', 'Telok Blangah')), datetime.datetime(2017, 1, 6, 6, 0))

#############
# Task 4b   #
#############

def get_schedules_near_loc_id_in_line(train_schedule, line, loc_id):
    return filter(
        lambda scheduleEvent: abs(loc_id - get_location_id_in_line(scheduleEvent, line)) <= 0.5, 
        train_schedule)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4B
# print("## Task 4b ##")
test_schedules_near_loc_id = get_schedules_near_loc_id_in_line(FULL_SCHEDULE[:10], CCL, test_loc_id1)
# print(test_schedules_near_loc_id[1])

# Expected Output #
# (('TRAIN 0-0',), (True, ('CC3', 'Esplanade'), ('CC4', 'Promenade')), datetime.datetime(2017, 1, 6, 6, 5))

#############
# Task 4c   #
#############

def get_rogue_schedules_in_line(train_schedule, line, time, loc_id):
    time_filtered = get_schedules_at_time(train_schedule, time)
    time_and_location_filtered = get_schedules_near_loc_id_in_line(time_filtered, line, loc_id)

    return time_and_location_filtered

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4C
# print("## Task 4c ##")
test_bd_event3 = VALID_BD_EVENTS[0]
test_loc_id3 = get_location_id_in_line(test_bd_event3, CCL)
test_datetime3 = get_schedule_time(test_bd_event3)
test_rogue_schedules = get_rogue_schedules_in_line(FULL_SCHEDULE[1000:1100], CCL, test_datetime3, test_loc_id3)
# print(test_rogue_schedules[2])

# Expected Output #
# (('TRAIN 1-11',), (True, ('CC24', 'Kent Ridge'), ('CC23', 'one-north')), datetime.datetime(2017, 1, 6, 7, 9))

############
## Task 5 ##
############

###############
# Scorer ADT  #
###############

def make_scorer():
    return {}

def blame_train(scorer, train_code):
    scorer[train_code] = scorer.get(train_code, 0) + 1
    return scorer

def get_blame_scores(scorer):
    return tuple(scorer.items())

# Use this to keep track of each train's blame score.
SCORER = make_scorer()

#############
# Task 5a   #
#############

def calculate_blame_in_line(full_schedule, valid_bd_events, line, scorer):
    for bd_event in valid_bd_events:
        loc_id = get_location_id_in_line(bd_event, line)
        time = get_schedule_time(bd_event)
        scheduleEvents = get_rogue_schedules_in_line(full_schedule, line, time, loc_id)
        rogue_train_set = set()

        for event in scheduleEvents:
            rogue_train = get_train(event)
            rogue_train_code = get_train_code(rogue_train)
            rogue_train_set.add(rogue_train_code)
        
        for rogue_train in rogue_train_set:
            blame_train(scorer, rogue_train)
    
    return scorer

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 5A. THIS IS NOT OPTIONAL TESTING!
calculate_blame_in_line(FULL_SCHEDULE, VALID_BD_EVENTS, CCL, SCORER)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5A
print("## Task 5a ##")
print(get_blame_scores(SCORER))
print(sorted(get_blame_scores(SCORER))[7])

# Expected Answer
# ('TRAIN 0-5', 2)

#############
# Task 5b   #
#############

def find_max_score(scorer):
    return max(map(lambda scores: scores[1], get_blame_scores(scorer)))

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5B
print("## Task 5b ##")
test_max_score = find_max_score(SCORER)
print(test_max_score)

# Expected answer
# 180

#############
# Task 5c   #
#############

# UNCOMMENT THE CODE BELOW TO VIEW ALL BLAME SCORES. THIS IS NOT OPTIONAL TESTING!
print("## Task 5c ##")
train_scores = get_blame_scores(SCORER)
print("############### Candidate rogue trains ###############")
for score in train_scores:
    print("%s: %d" % (score[0], score[1]))
print("######################################################")

''' Please type your answer into the Task 5c textbox on Coursemology '''

#############
# Task 5d   #
#############

def find_rogue_train(scorer, max_score):
    return filter(lambda score: score[1] == max_score, get_blame_scores(scorer))[0][0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5D
print("## Task 5d ##")
print('a', find_rogue_train(SCORER, test_max_score))
# print("Rogue Train is '%s'" % find_rogue_train(SCORER, test_max_score))

# Expected Answer
# Rogue Train is 'TRAIN 0-4'

# CS1010S --- Programming Methodology
#
# Mission 5
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

################ \/ MISSION 04 CODE HERE \/ ################

###############
# Station ADT #
###############

def make_station(station_code, station_name):
    return (station_code, station_name)

def get_station_code(station):
    return station[0]

def get_station_name(station):
    return station[1]

### \/ PLEASE UNCOMMENT THIS BEFORE STARTING MISSION 5 \/ ###
test_station1 = make_station('CC2', 'Bras Basah')
test_station2 = make_station('CC3', 'Esplanade')
test_station3 = make_station('CC4', 'Promenade')


#############
# Train ADT #
#############

def make_train(train_code):
    return (train_code,)

test_train = make_train('TRAIN 0-0')

def get_train_code(train):
    return train[0]

############
# Line ADT #
############

def make_line(name, stations):
    return (name, stations)

def get_line_name(line):
    return line[0]

def get_line_stations(line):
    return line[1]

def get_station_by_name(line, station_name):
    for station in get_line_stations(line):
        if get_station_name(station) == station_name:
            return station
    return None

def get_station_by_code(line, station_code):
    for station in get_line_stations(line):
        if get_station_code(station) == station_code:
            return station
    return None

def get_station_position(line, station_code):
    index = 0
    for station in get_line_stations(line):
        if get_station_code(station) == station_code:
            return index
        else:
            index += 1
    return -1

### \/ PLEASE UNCOMMENT THIS BEFORE STARTING MISSION 5 \/ ###
test_line = make_line('Circle Line', (test_station1, test_station2, test_station3))

#####################
# TrainPosition ADT #
#####################

def make_train_position(is_moving, from_station, to_station):
    ''' Do NOT modify this function'''
    return (is_moving, from_station, to_station)

def get_is_moving(train_position):
    return train_position[0]

def get_direction(line, train_position):
    if get_station_position(line, get_station_code(train_position[2])) > get_station_position(line, get_station_code(train_position[1])):
        return 0
    elif get_station_position(line, get_station_code(train_position[1])) > get_station_position(line, get_station_code(train_position[2])):
        return 1

def get_stopped_station(train_position):
    if get_is_moving(train_position) == False:
        return (train_position[1])
    return None

def get_previous_station(train_position):
    if get_is_moving(train_position) == True:
        return (train_position[1])
    return None

def get_next_station(train_position):
    return (train_position[2])

### \/ PLEASE UNCOMMENT THIS BEFORE STARTING MISSION  5 \/ ###
test_train_position1 = make_train_position(False, test_station1, test_station2)
test_train_position2 = make_train_position(True, test_station3, test_station2)

#####################
# ScheduleEvent ADT #
#####################

def make_schedule_event(train, train_position, time):
    return (train, train_position, time)

def get_train(schedule_event):
    return schedule_event[0]

def get_train_position(schedule_event):
    return schedule_event[1]

def get_schedule_time(schedule_event):
    return schedule_event[2]

### \/ PLEASE UNCOMMENT THIS BEFORE STARTING MISSION 5 \/ ###
test_bd_event1 = make_schedule_event(test_train, test_train_position2, datetime.datetime(2016, 1, 1, 9, 27))
test_bd_event2 = make_schedule_event(test_train, test_train_position1, datetime.datetime(2016, 1, 1, 2, 25))

################ /\ MISSION 04 CODE HERE /\ ################

############
## Task 1 ##
############

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows


###########
# Task 1a #
###########

def parse_lines(data_file):
    rows = read_csv(data_file)[1:]
    lines = ()
    curr_line_name = rows[0][2]
    curr_line_stations = ()
    for row in rows:
        code, station_name, line_name = row
        if line_name == curr_line_name:
            station = make_station(code, station_name)
            curr_line_stations = curr_line_stations + (station,)
        else:
            lines = lines + (make_line(curr_line_name, curr_line_stations),)
            curr_line_stations = ()
            curr_line_name = line_name
            station = make_station(code, station_name)
            curr_line_stations = curr_line_stations + (station,)
    lines = lines + (make_line(curr_line_name, curr_line_stations),)
    return lines  
    
# UNCOMMENT THE CODE BELOW WHEßßssN YOU ARE DONE WITH TASK 1A. THIS IS NOT OPTIONAL TESTING!
LINES = parse_lines('station_info.csv')
CCL = filter(lambda line: get_line_name(line) == 'Circle Line', LINES)[0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1A
print("## Task 1a ##")
print(get_line_stations(CCL)[5:8])

# Expected Output #
# (('CC6', 'Stadium'), ('CC7', 'Mountbatten'), ('CC8', 'Dakota'))


###########
# Task 1b #
###########

def parse_events_in_line(data_file, line):
    rows = read_csv(data_file)[1:]    
    events = ()
    for row in rows:
        train = make_train(row[0])
        from_position = get_station_by_code(line, row[2])
        to_position = get_station_by_code(line, row[3])
        if row[1] == "True":
            is_moving = True
        elif row[1] == "False":
            is_moving = False
        train_position = make_train_position(is_moving, from_position, to_position)
        time = datetime.datetime((int(row[4][6])*1000 + int(row[4][7])*100 + int(row[4][8])*10 + int(row[4][9])), (int(row[4][3])*10 + int(row[4][4])), (int(row[4][0])*10 + int(row[4][1])), (int(row[5][0])*10 + int(row[5][1])),(int(row[5][3])*10 + int(row[5][4])))
        schedule = make_schedule_event(train, train_position, time)
        events = events + (schedule,)
    return events

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 1B. THIS IS NOT OPTIONAL TESTING!
BD_EVENTS = parse_events_in_line('breakdown_events.csv', CCL)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1B
print("## Task 1b ##")
print(BD_EVENTS[9])

# Expected Output #
# (('TRAIN 1-11',), (False, ('CC23', 'one-north'), ('CC22', 'Buona Vista')), datetime.datetime(2017, 1, 6, 7, 9))


############
## Task 2 ##
############


###########
# Task 2a #
###########

def is_valid_event_in_line(bd_event, line):
    from_position = get_station_position(line, bd_event[1][1][0])
    to_position = get_station_position(line, bd_event[1][2][0])
    if 7 <= get_schedule_time(bd_event).hour:
        if (get_schedule_time(bd_event).hour <= 23 and get_schedule_time(bd_event).minute == 0) or (get_schedule_time(bd_event).hour <= 22 and get_schedule_time(bd_event).minute <= 59):
            if from_position:
                if to_position:
                    if abs(from_position - to_position) == 1:
                        return True
    return False
    
def get_valid_events_in_line(bd_events, line):
    ''' Do NOT modify this function'''
    return filter(lambda ev: is_valid_event_in_line(ev, line), bd_events)

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2A. THIS IS NOT OPTIONAL TESTING!
VALID_BD_EVENTS = get_valid_events_in_line(BD_EVENTS, CCL)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2A
print("## Task 2a ##")
print(is_valid_event_in_line(test_bd_event1, CCL))
print(is_valid_event_in_line(test_bd_event2, CCL))

# Expected Output #
# True
# False


###########
# Task 2b #
###########

def get_location_id_in_line(bd_event, line):
    train_position = get_train_position(bd_event)
    if get_is_moving(train_position) == False:
        location_id = get_station_position(line, get_station_code(get_stopped_station(train_position)))
    else:
        location_id = (get_station_position(line, get_station_code(get_previous_station(train_position))) + get_station_position(line, get_station_code(get_next_station(train_position))))/2
    return location_id
    

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2B
print("## Task 2b ##")
test_loc_id1 = get_location_id_in_line(test_bd_event1, CCL)
test_loc_id2 = get_location_id_in_line(test_bd_event2, CCL)
print(test_loc_id1)
print(test_loc_id2)

# Expected Output #
# 2.5
# 1


############
## Task 3 ##
############

# UNCOMMENT the following to read the entire train schedule
FULL_SCHEDULE = parse_events_in_line('train_schedule.csv', CCL)    # this will take some time to run


###########
# Task 3a #
###########

def get_schedules_at_time(train_schedule, time):
    events = ()
    for schedule_event in train_schedule:
        if get_schedule_time(schedule_event) == time:
            events = events + (schedule_event,)
        else:
            events = events
    return events

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3A
print("## Task 3a ##")
test_datetime = datetime.datetime(2017, 1, 6, 6, 0)
test_schedules_at_time = get_schedules_at_time(FULL_SCHEDULE[:5], test_datetime)
print(test_schedules_at_time[1])

# Expected Output #
# (('TRAIN 1-0',), (False, ('CC29', 'HarbourFront'), ('CC28', 'Telok Blangah')), datetime.datetime(2017, 1, 6, 6, 0))


###########
# Task 3b #
###########

def get_schedules_near_loc_id_in_line(train_schedule, line, loc_id):
    events = ()
    for schedule_event in train_schedule:
        if abs(get_location_id_in_line(schedule_event, line) - loc_id) <= 0.5:
            events = events + (schedule_event,)
        else:
            events = events
    return events 
    

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3B
# print("## Task 3b ##")
test_schedules_near_loc_id = get_schedules_near_loc_id_in_line(FULL_SCHEDULE[:10], CCL, test_loc_id1)
print(test_schedules_near_loc_id[1])

# Expected Output #
# (('TRAIN 0-0',), (True, ('CC3', 'Esplanade'), ('CC4', 'Promenade')), datetime.datetime(2017, 1, 6, 6, 5))


###########
# Task 3c #
###########

# function takes in a tuple of schedules and only returns those near an timely schedules in another tuple


def get_rogue_schedules_in_line(train_schedules, line, time, loc_id):
    events = get_schedules_at_time(train_schedules, time)
    events = get_schedules_near_loc_id_in_line(events, line, loc_id)
    return events

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3C
print("## Task 3c ##")
test_bd_event3 = VALID_BD_EVENTS[0]
test_loc_id3 = get_location_id_in_line(test_bd_event3, CCL)
test_datetime3 = get_schedule_time(test_bd_event3)
test_rogue_schedules = get_rogue_schedules_in_line(FULL_SCHEDULE[1000:1100], CCL, test_datetime3, test_loc_id3)
print(test_rogue_schedules[2])

# Expected Output #
# (('TRAIN 1-11',), (True, ('CC24', 'Kent Ridge'), ('CC23', 'one-north')), datetime.datetime(2017, 1, 6, 7, 9))


############
## Task 4 ##
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


###########
# Task 4a #
###########

def calculate_blame_in_line(full_schedule, valid_bd_events, line, scorer):
    rogue_schedules = ()
    for bd_event in valid_bd_events:
        rogue_schedule_in_line = get_rogue_schedules_in_line(full_schedule, line, get_schedule_time(bd_event), get_location_id_in_line(bd_event, line))
        # all train scehdules to blamed * 2

        int_schedule = ()
        train_code = ()
        for rogue_schedule in rogue_schedule_in_line:
            if get_train_code(get_train(rogue_schedule)) not in train_code:
                int_schedule = int_schedule + (rogue_schedule,)
                train_code = train_code + (get_train_code(get_train(rogue_schedule)),)
            elif get_train_code(get_train(rogue_schedule)) in train_code:
                int_schedule = int_schedule
        
        rogue_schedules = rogue_schedules + int_schedule
        
    for rogue_schedule in rogue_schedules:
        train_code_rogue_train = get_train_code(get_train(rogue_schedule))
        blame_train(scorer, train_code_rogue_train)
        
    return scorer

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 4A. THIS IS NOT OPTIONAL TESTING!
calculate_blame_in_line(FULL_SCHEDULE, VALID_BD_EVENTS, CCL, SCORER)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4A
print("## Task 4a ##")
print(sorted(get_blame_scores(SCORER))[7])

# Expected Answer
# ('TRAIN 0-5', 2)


###########
# Task 4b #
###########

# a = map((lambda x: x ** 2), x)
# max function

def find_max_score(scorer):
    train_scores = map((lambda x: x[1]), get_blame_scores(scorer))
    maximum = max(train_scores)
    return maximum

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4B
print("## Task 4b ##")
test_max_score = find_max_score(SCORER)
print(test_max_score)

# Expected answer
# 180


###########
# Task 4c #
###########

# UNCOMMENT THE CODE BELOW TO VIEW ALL BLAME SCORES. THIS IS NOT OPTIONAL TESTING!
print("## Task 4c ##")
train_scores = get_blame_scores(SCORER)
print("############### Candidate rogue trains ###############")
for score in train_scores:
    print("%s: %d" % (score[0], score[1]))
print("######################################################")

''' Yes as one train, TRAIN 0-4 has a blames score of 180. Meanwhile the next highest blame score is 17 of trains, TRAIN 1-11 and TRAIN 0-12. This shows that TRAIN 0-4 has a blame score much higher than any other train. This indicates that this train is near to most of the breakdown events. Therefore it can be identified as the single rouge train that is causing the breakdowns. '''


###########
# Task 4d #
###########

def find_rogue_train(scorer, max_score):
    for score in get_blame_scores(scorer):
        if max_score == score[1]:
            return score[0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4D
print("## Task 4d ##")
print("Rogue Train is '%s'" % find_rogue_train(SCORER, test_max_score))

# Expected Answer
# Rogue Train is 'TRAIN 0-4'


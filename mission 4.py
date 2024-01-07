def make_station(station_code, station_name):
    return (station_code, station_name)

# e.g input
# esplanade = make_station("CC2", "Esplanade")

def get_station_code(station):
    return station[0]

def get_station_name(station):
    return station[1]

################################

def make_train(train_code):
    return (train_code,)

# e.g input
# train = make_train("0-0")

def get_train_code(train):
    return train[0]


################################

def make_line(name, tuple_of_stations):
    return (name, tuple_of_stations)

# e.g input
# circle_line = make_line("Circle line", (('CC2', 'Bras Basah'), ('CC3', 'Esplanade'), ('CC4', 'Promenade')))

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

################################

def make_train_position(is_moving, from_station, to_station):
    return (is_moving, from_station, to_station)

# e.g input
# train_position = make_train_position(False, ('CC4', 'Promenade'), ('CC2', 'Bras Basah'))

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

################################

def make_schedule_event(train, train_position, time):
    return (train, train_position, time)

# e.g input
# make_schedule_event

# train = make_train("0-0")
# train_position = make_train_position(False, ('CC4', 'Promenade'), ('CC2', 'Bras Basah'))
# my_datetime = datetime.datetime(2017, 2, 28, 13, 5)

def get_train(schedule_event):
    return schedule_event[0]

def get_train_position(schedule_event):
    return schedule_event[1]

def get_schedule_time(schedule_event):
    return schedule_event[2]
    
    




    































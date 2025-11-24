#metro database as mdb
def load_data():
    database = {}
    f = open("metro_data.txt", "r")
    
    for line in f:
        # Split line and clean spaces in one go
        line_name, stn, time = [x.strip() for x in line.split('|')]
        
        if line_name not in database:
            database[line_name] = []
        
        database[line_name].append((stn, int(time)))
            
    f.close()
    return database

# Load Database
mdb = load_data()

def time_to_min(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

def min_to_time(min):
    h = min // 60
    m = min % 60
    return f"{h:02}:{m:02}"

def next_train(ct):
    st = 6 * 60  # 360 mins (06:00) #st = 1st train time
    et = 23 * 60   # 1380 mins (23:00) #et = last train time
    if ct < st: print("Next train at 06:00 AM") #ct = current time
    if ct >= et: print("No more trains today")


    train_time = st
    while train_time <= et:
        # Check Peak Hours (8-10 and 17-19 hours)
        if (480 <= train_time < 600) or (1020 <= train_time < 1140) :
            interval = 4 
        else :
            interval = 8
        
        if train_time >= ct:
            return train_time
        train_time += interval
    return

def find_station(station):
    """Finds which line a station is on"""
    line = []
    for line_name, stations in mdb.items():
        for stn, time in stations:
            if stn.lower() == station.lower():
                line.append((line_name, time))
    return line

# --- MAIN PROGRAM ---
 
start = input("Source Station: ").strip()
stop = input("Destination Station: ").strip()
time = input("Current Time (HH:MM): ").strip()  
print(" ")

min_time = time_to_min(time)
stat_info = find_station(start)
stop_info = find_station(stop)

start_dict = dict(stat_info)
stop_dict = dict(stop_info)

if not stat_info:
    print(f"Station '{start}' not found!")
    exit()


for destination_line, destination_time in stop_info:

    if destination_line in start_dict:
        start_time = start_dict[destination_line]

        travel_time = abs(destination_time - start_time)
        dept_time = next_train(min_time)
        
        print(f"Direct Route ({destination_line} Line)")
        print(" ")
        print(f"Next Train: {min_to_time(dept_time)}")
        print(f"Arrival: {min_to_time(dept_time + travel_time)}")
        print(f"Travel Time: {travel_time} mins")
        exit()

interchange = ["Janakpuri West", "Botanical Garden", "Yamuna Bank"]
best_time = 2000
best_plan = None

for switch in interchange:
    switch_dict = dict(find_station(switch)) 

    line1 = None
    for line in switch_dict:
        if line in start_dict:
            line1 = line
            break

    line2 = None
    for line in switch_dict:
        if line in stop_dict:
            line2 = line
            break

    if line1 and line2 and line1 != line2:
        t1 = abs(switch_dict[line1] - start_dict[line1])
        t2 = abs(stop_dict[line2] - switch_dict[line2])

        dept_1 = next_train(min_time)
        
        arrived_interchanged = dept_1 + t1
        
        # Add 5 mins to walk to next platform
        dept_2 = next_train(arrived_interchanged + 5) 
        arrived_Destination = dept_2 + t2

        if arrived_Destination < best_time:
            best_time = arrived_Destination
            total_min = arrived_Destination - dept_1
            best_plan = [line1, min_to_time(dept_1), switch, min_to_time(arrived_interchanged), 
                         line2, min_to_time(dept_2), min_to_time(arrived_Destination)]

if best_plan:
    print(f"Interchange Route")
    print(" ")
    print(f"1. Take {best_plan[0]} Line at {best_plan[1]}")
    print(f"2. Arrive {best_plan[2]} at {best_plan[3]}")
    print(f"3. Switch to {best_plan[4]} (Next train: {best_plan[5]})")
    print(f"4. Reach Destination at {best_plan[6]}")
    print(f"5. Travel Time: {total_min} mins")
    exit()

if not best_plan:
    start_line = list(start_dict.keys())[0]
    end_line = list(stop_dict.keys())[0]

    if (start_line == "Magenta" and end_line == "Blue-Branch") or (start_line == "Blue-Branch" and end_line == "Magenta"):
        entry_points = ["Janakpuri West", "Botanical Garden"]

        for switch in entry_points:
            switch_dict = dict(find_station(switch))
            yamuna_dict = dict(find_station("Yamuna Bank"))

            line1 = start_line
            line2 = "Blue"
            line3 = end_line

            t1 = abs(switch_dict[line1] - start_dict[line1])
            t2 = abs(yamuna_dict["Blue"] - switch_dict["Blue"])
            t3 = abs(stop_dict[line3] - yamuna_dict[line3])
            dept_1 = next_train(min_time)
            arrived_switch1 = dept_1 + t1
            dept_2 = next_train(arrived_switch1 + 5)
            arrived_yamuna = dept_2 + t2
            dept_3 = next_train(arrived_yamuna + 5)
            arrived_Destination = dept_3 + t3
            if arrived_Destination < best_time:
                best_time = arrived_Destination
                total_min = arrived_Destination - dept_1
                best_plan = [line1, min_to_time(dept_1), switch, min_to_time(arrived_switch1),
                             line2, min_to_time(dept_2), "Yamuna Bank", min_to_time(arrived_yamuna),
                             line3, min_to_time(dept_3), min_to_time(arrived_Destination)]

    print(f"Double Interchange Route")
    print(" ")
    print(f"1. Take {best_plan[0]} at {best_plan[1]}")
    print(f"2. Switch at {best_plan[2]} ({best_plan[3]})")
    print(f"3. Take {best_plan[4]} at {best_plan[5]}")
    print(f"4. Switch at {best_plan[6]} ({best_plan[7]})")
    print(f"5. Take {best_plan[8]} at {best_plan[9]}")
    print(f"6. Arrive Destination at {best_plan[10]}")
    print(f"Total Time: {total_min} mins")


else:
    print("No route found.")


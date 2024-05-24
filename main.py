mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970] 
mission_success = [True, False, True, True, True, True, False]

# Initialize counters
total_missions = 0
successful_missions = 0

# List to store missions launched before 2000
missions_before_2000 = []

# Iterate through the list of missions
for name, year, success in zip(mission_names, mission_years, mission_success):
    total_missions += 1
    if success:
        successful_missions += 1
    if year < 2000:
        missions_before_2000.append(name)

# Calculate success rate
success_rate = (successful_missions / total_missions) * 100

# Output the Results
print("Total number of missions:", total_missions)
print("Number of successful missions:", successful_missions)
print("Success rate of missions: {:.2f}%".format(success_rate))
print("Missions launched before the year 2000:", missions_before_2000)
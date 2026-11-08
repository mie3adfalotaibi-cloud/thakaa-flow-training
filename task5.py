distance = float(input("Distance (million km): "))
earth_age = int(input("Your age (Earth years): "))
earth_weight = float(input("Your weight on Earth (kg): "))

# Message travel time
seconds_one_way = distance * 1000000 / 299792
minutes = int(seconds_one_way // 60)
seconds = int(seconds_one_way % 60)

# Round trip time
round_trip = seconds_one_way * 2
rt_minutes = int(round_trip // 60)
rt_seconds = int(round_trip % 60)

# Age on Mars
mars_age = earth_age * (687 / 365.25)

# Weight on Mars
mars_weight = earth_weight * 0.38

# Earth week in Mars sols
mars_sol_hours = 24 + (39 / 60) + (35 / 3600)
mars_sols = (7 * 24) / mars_sol_hours

print("=== MARS MISSION REPORT ===")
print(f"Message travel time: {minutes} min {seconds} sec")
print(f"Round trip: {rt_minutes} min {rt_seconds} sec")
print(f"Your age on Mars: {mars_age:.2f} years")
print(f"Your weight on Mars: {mars_weight:.2f} kg")
print(f"One Earth week = {mars_sols:.2f} Mars sols")

# Direct video calls with Mars are difficult because
# there is a communication delay between Earth and Mars.
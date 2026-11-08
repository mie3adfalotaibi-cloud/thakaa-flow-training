MISSION_DAYS = 70
crew = ("Nora", "Omar", "Lina", "Yousef")
supplies = {"oxygen_kg": 840, "water_l": 1260, "food_kg": 336}
per_person_daily = {"oxygen_kg": 0.84, "water_l": 3.5, "food_kg": 1.2}
telescope_a = {"Kepler-22b", "Proxima b", "TRAPPIST-1e", "Gliese 667Cc"}
telescope_b = {"Proxima b", "TRAPPIST-1e", "HD 40307g"}

# 1) days each supply lasts for the whole crew
n = len(crew)
days_left = {
    "oxygen_kg": supplies["oxygen_kg"] / (per_person_daily["oxygen_kg"] * n),
    "water_l": supplies["water_l"] / (per_person_daily["water_l"] * n),
    "food_kg": supplies["food_kg"] / (per_person_daily["food_kg"] * n)
}
print("Days left:", days_left)

# 2) weakest supply
weakest = min(days_left, key=days_left.get)
print("Weakest:", weakest, "-", days_left[weakest], "days")
# key=days_left.get tells min() to compare the values (days), not the key names.

# 3) is it enough?
if days_left[weakest] >= MISSION_DAYS:
    print("Enough supplies for", MISSION_DAYS, "days")
else:
    missing_days = MISSION_DAYS - days_left[weakest]
    needed = per_person_daily[weakest] * n * MISSION_DAYS
    missing = needed - supplies[weakest]
    print("Not enough! Short by", missing_days, "days, missing", missing, weakest)

# 4) with MISSION_DAYS = 70 the food lasts exactly 70 days.
# I used >= so exactly equal counts as enough.
# Result: with 75 -> Not enough (short 5 days, 24 kg food). With 70 -> Enough.

# 5) telescopes
print("Seen by both:", sorted(telescope_a & telescope_b))
print("Only A:", sorted(telescope_a - telescope_b))
print("All planets:", len(telescope_a | telescope_b))

# 6) mission log
mission_log = []
mission_log.append("Day 1: Launch from Earth")
mission_log.append("Day 20: Solar storm, shields up")
mission_log.append("Day 45: Repaired the water system")
print("Last event:", mission_log[-1])
print("Number of events:", len(mission_log))

# 7) crew is a tuple because the crew must not change during the mission.
# A tuple cannot be changed, so no one can add or remove a member by mistake.
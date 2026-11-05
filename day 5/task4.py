trainees = [
    {"name": "Sara", "checkin": "09:40", "on_time": 5, "report_on_time": False, "scores": [8, 8, 8, 8, 8]},
    {"name": "Omar", "checkin": "10:15", "on_time": 4, "report_on_time": True, "scores": [9, 9, 9, 9, 0]},
    {"name": "Lina", "checkin": "08:55", "on_time": 5, "report_on_time": True, "scores": [10, 9, 9, 10, 8]},
]
total_tasks = 5


# 1) time to minutes
def to_minutes(time_text):
    parts = time_text.split(":")
    return int(parts[0]) * 60 + int(parts[1])


# 2) daily points
def daily_points(checkin, on_time, total_tasks, report_on_time, scores):
    points = 0
    if to_minutes(checkin) < 600:
        points = points + 5
    if report_on_time:
        points = points + 5
    if total_tasks > 0:
        points = points + 10 * (on_time / total_tasks)
        points = points + 10 * (sum(scores) / (10 * total_tasks))
    return points


# 5) add myself: 0.4 more than Lina
trainees.append({"name": "Mieaad", "checkin": "09:00", "on_time": 5, "report_on_time": True, "scores": [10, 10, 10, 9, 9]})

# 3) calculate and save points
for t in trainees:
    t["points"] = daily_points(t["checkin"], t["on_time"], total_tasks, t["report_on_time"], t["scores"])
    print(f"{t['name']}: {t['points']:.1f} points")

# 4) total, average, best of the day
total_points = 0
best = trainees[0]
for t in trainees:
    total_points = total_points + t["points"]
    if t["points"] > best["points"]:
        best = t

print(f"Total points: {total_points:.1f}")
print(f"Average: {total_points / len(trainees):.1f}")
print(f"Best of the Day: {best['name']} ({best['points']:.1f})")

# 5) difference between me and Lina
print("Difference:", trainees[3]["points"] - trainees[2]["points"])
print(f"Difference rounded: {trainees[3]['points'] - trainees[2]['points']:.1f}")
# Lina has 46 out of 50 in quality (9.2). I need 9.6, so my scores add up to 48.
# Everything else is full for both of us, so the difference is exactly 0.4.
# But Python printed 0.3999999999999986, because computers store decimals
# in binary and some numbers like 0.4 cannot be stored exactly. So I used :.1f.

# 6) day with no tasks
print("No tasks day:", daily_points("09:00", 0, 0, True, []))
# No error: total_tasks is 0, so we skip the tasks and quality points.
# Only check-in (5) and report (5) = 10.
hour = int(input("hour (0-23):"))
minute = int(input("Minute (0-59):"))

if hour < 0 or hour > 23 or minute < 0 or minute > 59:
    print("Invalid time")
else:
    total = hour * 60 + minute
    if total < 600:
        print("On time +5")
    elif total < 1020:
        print("Late, no points")
    else:
        print("Training day is over")
        # 10:00 counts as late because total = 600, and the first condition is < 600, so 10:00 is not less than 600 and goes to the elif.
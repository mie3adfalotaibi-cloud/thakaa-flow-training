registered = ["sara@mail.com", "omar@mail.com", "lina@mail.com",
              "sara@mail.com", "yousef@mail.com", "nora@mail.com"]
attended = ["omar@mail.com", "lina@mail.com", "khaled@mail.com", "nora@mail.com"]
tickets = ["VIP", "Regular", "Regular", "Student", "VIP", "Regular"]
prices = {"VIP": 450, "Regular": 200, "Student": 100}

# 1) duplicates
reg_set = set(registered)
att_set = set(attended)
duplicates = len(registered) - len(reg_set)

# 2) set operations
both = reg_set & att_set
no_show = reg_set - att_set
walk_in = att_set - reg_set

# 3) attendance rate
rate = len(both) / len(reg_set) * 100

# 4) ticket counts and revenue
ticket_counts = {
    "VIP": tickets.count("VIP"),
    "Regular": tickets.count("Regular"),
    "Student": tickets.count("Student")
}
revenue = (ticket_counts["VIP"] * prices["VIP"]
           + ticket_counts["Regular"] * prices["Regular"]
           + ticket_counts["Student"] * prices["Student"])

# 5) report
print("===== Workshop Report =====")
print("Duplicate registrations:", duplicates)
print("Registered and attended:", sorted(both))
print("Registered, did not attend:", sorted(no_show))
print("Attended without registering:", sorted(walk_in))
print(f"Attendance rate: {rate:.1f}%")
print("Tickets:", ticket_counts)
print("Total revenue:", revenue, "SAR")

# 6) set has no order. Python stores set items in its own way (by hash),
# so print(set(registered)) can show a different order. Use sorted() to fix the order.
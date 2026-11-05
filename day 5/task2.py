days = ["Sun", "Mon", "Tue", "Wed", "Thu"]
sales = [1200, 950, 1800, 1430, 2100]

total = 0
best_index = 0
above = 0

for i in range(len(sales)):
    print(f"{days[i]}: {sales[i]} SAR")
    total = total + sales[i]
    if sales[i] > sales[best_index]:
        best_index = i
    if sales[i] > 1500:
        above = above + 1

average = total / len(sales)

print(f"Total: {total} SAR")
print(f"Average: {average:.0f} SAR")
print(f"Best day: {days[best_index]} ({sales[best_index]} SAR)")
print(f"Days above target: {above}")

# I used range(len(sales)) because I need the index i
# to get the day name from days[i] and the sale from sales[i] at the same time.
# With "for s in sales" I only get the number, not the day name.
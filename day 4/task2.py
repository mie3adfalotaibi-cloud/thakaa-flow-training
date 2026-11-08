tasks = ["Update website", "Client meeting", "Code review"]

# 1) add at the end and at the start
tasks.append("Write report")
tasks.insert(0, "Fix urgent bug")
print(tasks)

# 2) remove finished task
tasks.remove("Client meeting")
print(tasks)

# 3) add a task with my name, then pop it
tasks.append("Review Mieaad's code")
removed = tasks.pop()
print("Removed:", removed)

# 4) count, first, last, position
print("Number of tasks:", len(tasks))
print("First task:", tasks[0])
print("Last task:", tasks[-1])
print("Code review position:", tasks.index("Code review") + 1)

# 5) sorted copy vs original
print("Sorted copy:", sorted(tasks))
print("Original:", tasks)

# 6) try sort()
tasks.sort()
print("After sort():", tasks)

# sorted(tasks) makes a new sorted list and the original stays the same.
# tasks.sort() changes the original list itself.
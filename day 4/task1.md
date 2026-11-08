# Task 1

## Part 1: table

| Structure | Ordered? | Changeable? | Duplicates? | Access | Example |
|---|---|---|---|---|---|
| list | Yes | Yes | Yes | by index: x[0] | ["tea", "milk", "tea"] |
| tuple | Yes | No | Yes | by index: x[0] | (24.7, 46.6) |
| set | No | Yes | No | no index, use `in` | {"Python", "SQL"} |
| dict | Yes | Yes | keys: No | by key: x["name"] | {"name": "Mieaad"} |

## Part 2: predict the output

| Line | Prediction | Actual | Reason |
|---|---|---|---|
| print(skills, len(skills)) | ['Python', 'Excel', 'Git', 'SQL', 'Pandas'] 5 | same | insert(1) puts Excel at position 1 |
| print(skills[1], skills[-1], skills[1:3]) | Excel Pandas ['Excel', 'Git'] | same | [1:3] takes 1 and 2, stops before 3 |
| print(len(ids), 104 in ids) | 3 False | same | set removes the duplicate 101 |
| print(emp.get("team", "Not set")) | Not set | same | team key does not exist yet |
| print(len(emp), list(emp.keys())) | 3 ['name', 'role', 'team'] | same | we added team |

## Part 3: common trap

Output:
[1, 2, 3, 4]
[1, 2, 3, 4] [1, 2, 3, 4, 5]

b = a does not make a new list. a and b are two names for the same list, like two keys to the same room.
a.copy() makes a new separate list, so changing c does not change a.

## Part 4: which structure?

- Branch coordinates on the map: tuple, because they never change.
- Today's tasks in order: list, because order matters and it changes.
- Client company names without duplicates: set, because it removes duplicates.
- Employee data (name, title, team): dict, because each value has a name (key).

My examples: tuple = my birth date, list = my shopping list, set = cities I visited, dict = my profile.
# Task 1

## Part 1: for vs while

for: used when I know how many times to repeat, or I go over a list.
Example: send a reminder to each trainee in a list of 20 names.

while: used when I repeat until a condition changes, and I don't know how many times.
Example: keep asking for the password until the user types it correctly.

## Part 2: predict the output

| Code | Prediction | Actual | Reason |
|---|---|---|---|
| x = add(2, 3) | 5 | 5 | add prints a + b |
| print(x, y) | None 6 | None 6 | add has no return, so x is None. multiply returns 6 |
| for i in range(1, 10, 3) | 1 4 7 | 1 4 7 | starts at 1, step 3, stops before 10 |
| while count > 0 | Attempt 3, Attempt 2, Attempt 1 | same | count goes down by 1 until 0 |

None appears because add() only prints the result and does not return it.
print shows the value on the screen only. return sends the value back so I can save it in a variable and use it later.

## Part 3: trace table (photo attached)

| Round | i | total |
|---|---|---|
| start | 1 | 0 |
| 1 | 2 | 2 |
| 2 | 3 | 6 |
| 3 | 4 | 12 |
| 4 | 5 | 20 |
| 5 | 6 | 30 |

Output: 30. The loop stops when i = 6 because 6 <= 5 is False.

## Part 4: infinite loop

An infinite loop is a loop that never stops because its condition stays True forever.
If we delete i = i + 1, i stays 1, so i <= 5 is always True and the program never ends.
I stopped it with Ctrl + C in the terminal.
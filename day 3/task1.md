# Task 1

## Part 1: email code

| Line | My prediction | Actual output | Reason if different |
|------|---------------|---------------|---------------------|
| print(clean.lower()) | sara.ahmed@tfco.sa | sara.ahmed@tfco.sa | same |
| print(email.count("a"), clean.lower().count("a")) | 2 4 | 2 4 | same |
| print("tfco" in email, "tfco" in clean.lower()) | False True | False True | same |
| print(clean.startswith("sara")) | False | False | same |
| print(len(email), len(clean)) | 21 18 | 21 18 | same |
| print(clean[:4], clean[-2:]) | Sara SA | Sara SA | same |

## Part 2: score bug

The code never prints Excellent because 95 >= 60 is true first, so Python stops there.

Fixed:
```python
score = 95
if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Pass")
else:
    print("Fail")
```

Rule: put the strictest (highest) condition first, because Python runs only the first true branch.

## Part 3: x = 7

1. `x > 3 and x % 2 == 0` -> True and (7 % 2 = 1, and 1 == 0 is False) -> False
2. `not (x < 2) or x == 6` -> not False = True, so True or ... -> True
3. `x * 2 >= 7 and not x == 5` -> 14 >= 7 is True, not (False) is True -> True

## Part 4: security

Username: users may type extra spaces or capital letters (" Admin "), so strip() and lower() make it match "admin".
Password: it is case-sensitive, so lower() makes "Pass" and "pass" the same.
That reduces the possible passwords and makes them easier to guess.
So lower() on a password is a security mistake.
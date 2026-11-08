name = input("Name: ")
email = input("Email: ")
phone = input("Phone: ")

# clean
name = name.strip().title()
while "  " in name:
    name = name.replace("  ", " ")
email = email.replace(" ", "").lower()
phone = phone.replace(" ", "")

# validate
name_ok = len(name) > 0
email_ok = "@" in email and "." in email and not email.startswith("@")
phone_ok = phone.isdigit() and phone.startswith("05") and len(phone) == 10

if not name_ok:
    print("Error: name is empty")
if not email_ok:
    print("Error: invalid email")
if not phone_ok:
    print("Error: phone must be 10 digits and start with 05")

if name_ok and email_ok and phone_ok:
    print(f"{name} | {email} | {phone} OK")
    space = name.find(" ")
    if space == -1:
        first = name.lower()
    else:
        first = name[:space].lower()
    print(f"Suggested username: {first}.{phone[-2:]}")
# Test 1: task example -> OK
# Test 2: my own data -> OK
# Test 3: wrong phone -> error message
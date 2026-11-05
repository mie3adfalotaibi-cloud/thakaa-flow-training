def add_vat(amount, rate=0.15):
    return round(amount * (1 + rate), 2)


def format_price(amount):
    return f"{amount:,.2f} SAR"


def is_valid_phone(phone):
    phone = phone.replace(" ", "")
    return phone.isdigit() and phone.startswith("05") and len(phone) == 10


# 4) test each function with 3 values (one is wrong)
print(add_vat(100))
print(add_vat(200, 0.05))
print(add_vat(-50))
print(format_price(1234.5))
print(format_price(0))
print(format_price(1000000))
print(is_valid_phone("0551234567"))
print(is_valid_phone("055 123 4567"))
print(is_valid_phone("05abc12345"))

# 5) use them together
print(format_price(add_vat(1000)))

# 6) valid phones only
phones = ["0551234567", "0661234567", "055 123 4567", "05512", "05abc12345"]
valid_count = 0
for p in phones:
    if is_valid_phone(p):
        print("Valid:", p)
        valid_count = valid_count + 1
print("Number of valid phones:", valid_count)
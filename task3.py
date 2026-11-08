customer = input("Customer name: ")
product = input("Product: ")
price = float(input("Unit price: "))
quantity = int(input("Quantity: "))

subtotal = price * quantity
discount = subtotal * 0.10
after_discount = subtotal - discount
vat = after_discount * 0.15
total = after_discount + vat

print("========= INVOICE =========")
print(f"Customer: {customer}")
print(f"Product: {product} x {quantity}")
print(f"Subtotal: {subtotal:.2f} SAR")
print(f"Discount (10%): {discount:.2f} SAR")
print(f"After Discount: {after_discount:.2f} SAR")
print(f"VAT (15%): {vat:.2f} SAR")
print(f"Total: {total:.2f} SAR")

# I used float for price because prices can contain decimal values.
# I used int for quantity because quantities are whole numbers.
# If the user enters 2.5 for quantity, int() will raise a ValueError
# because it cannot convert a decimal number directly into an integer.

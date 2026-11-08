customer = input("Customer name: ")
service = input("Service: ")
date = input("Date: ")
time = input("Time: ")
service_price = float(input("Service price: "))
booking_no = int(input("Booking number: "))
session_minutes = int(input("Session length (minutes): "))

deposit = service_price * 0.30
remaining = service_price - deposit

hours = session_minutes // 60
minutes = session_minutes % 60

booking_code = f"TF-2026-{booking_no:04d}"

print(f"Hello {customer},")
print(f'Your booking for "{service}" is confirmed.')
print(f"Date: {date} at {time}")
print(f"Session length: {hours} h {minutes} min")
print(f"Booking code: {booking_code}")
print(f"Deposit due: {deposit:.2f} SAR")
print(f"Remaining on delivery: {remaining:.2f} SAR")
print("Thank you for choosing Thakaa Flow!")

# Bonus:
# If the discount changes to 25%, update the calculation percentage only.
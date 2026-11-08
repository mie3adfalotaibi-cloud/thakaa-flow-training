products = float(input("Products value: "))
city = input("City: ")
weight = float(input("Weight (kg): "))
coupon = input("Coupon (leave empty if none): ")

city = city.strip().lower()
coupon = coupon.strip().upper()

# shipping by city
if city == "riyadh":
    shipping = 15
elif city == "jeddah" or city == "dammam":
    shipping = 20
else:
    shipping = 30

# extra weight: 2 SAR per kg above 5
if weight > 5:
    shipping = shipping + (weight - 5) * 2

# coupon
discount = 0
if coupon == "TF10":
    if products >= 100:
        discount = products * 0.10
    else:
        print("TF10 needs products value of at least 100 SAR")
elif coupon == "FREESHIP":
    shipping = 0
elif coupon != "":
    print("Invalid coupon")

after_discount = products - discount

# free shipping for big orders
if after_discount >= 300:
    shipping = 0

vat = (after_discount + shipping) * 0.15
total = after_discount + shipping + vat

print(f"Products after discount: {after_discount:.2f} SAR")
print(f"Shipping: {shipping:.2f} SAR")
print(f"VAT: {vat:.2f} SAR")
print(f"Total: {total:.2f} SAR")
# Test 1: 280, riyadh, 6.5, tf10 -> total 310.50 (OK)
# Test 2: 80, abha, 3, tf10 -> TF10 message, total 126.50 (OK)
# Test 3: 350, jeddah, 9, no coupon -> free shipping, total 402.50 (OK)
# Test 4: 245, riyadh, 4.75, freeship -> total 281.75 (OK)
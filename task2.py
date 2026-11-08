name = "Mieaad"
city = "Riyadh"
major = "AI Diploma"
age = 21
coded_before = True
study_hours = 2.5

print("=== " + name + " ===")
print("city: " + city)
print("major: " + major)
print("age: " + str(age))
print("coded before: " + str(coded_before))
print("study hours: " + str(study_hours))
print()
print(f"=== {name} ===")
print(f"City: {city}")
print(f"Major: {major}")
print(f"Age: {age}")
print(f"Coded before: {coded_before}")
print(f"Study hours: {study_hours}")
print()
print(f"=== {name} ===\nCity: {city}\nMajor: {major}\nAge: {age}\nCoded before: {coded_before}\nStudy hours: {study_hours}")
print()
print(type(name), type(city), type(major))
print(type(age), type(coded_before), type(study_hours))
# f-string is easier for me because I write the variables inside the text, with no + or str().

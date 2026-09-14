card = "1234-5678-9012-3456"
masked = "XXXX-XXXX-XXXX-" + card[-4:]
print(masked)

phone_number = "09368065971"
hidden= phone_number[:4] + "****" + phone_number[-3:]
print(hidden)

date = "2024-0-29"
year = date[-4]


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

first_initial = first_name.title()[0].lower()
last_initial = last_name.title()[0].lower()

print(f"Your initials are: {first_initial}.{last_initial}")
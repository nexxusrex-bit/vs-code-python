principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principal amount: "))
    if principle <= 0:
        print("The principal cannot be less than or equal to zero.")

while True:
    rate = float(input("Enter the rate of interest rate: "))
    if rate < 0:
        print("The rate of interest rate cannot be less than to zero.")
    else:
        break

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("The time cannot be less than or equal to zero.")

total = principle * pow((1 + rate / 100), time)

print(f"The total amount after {time} years is: {total:.2f}")
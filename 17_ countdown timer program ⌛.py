import time 

time.sleep(1)
print("Hello! Welcome to the countdown timer program.")

alarm_time = int(input("Please enter the countdown time in seconds: "))

for i in range(alarm_time, 0, -1):
    print(i)
    time.sleep(1)

print("Time's up!")

alarm_time = int(input("Please enter the countdown time in seconds: "))
for x in range(alarm_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's up!")
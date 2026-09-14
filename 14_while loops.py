age = int(input("Please enter your age: "))
while age < 0:
    print("Age cannot be negative. Please enter a valid age.")
    age = int(input("Please enter your age: "))

#print(f"Thank you! Your age is {age}.")

name = input("Please enter your name: ")
while not name.islower() and not name.isupper():
    print("Name must contain only uppercase letters. Please enter a valid name.")
    name = input("Please enter your name: ")

print(f"Thank you! Your name is {name}.")
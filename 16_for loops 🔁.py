for x in range(5, 11, 2):
    print(x)
print("Done")

for x in reversed(range(1, 11)):
    print(x)
print("Done")

name = "JOSHUA"
for letter in name:
    print(letter)

name = "OMOSLAB"
for letter in reversed(name):
    print(letter)

for x in range(1, 11):
    if x % 2 == 0:
        print(x)

for x in range(1, 11):
    if x == 5:
        continue
    else:
        print(x) 
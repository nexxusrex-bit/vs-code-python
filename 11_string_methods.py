user_name = input("Enter your user name: ")
print("Your user name should be less than 12 characters, contain no spaces, and only contain letters.")

if len (user_name) > 12:
    print("Your user name can't be more than 12 characters.")
elif not user_name.find(" ") == -1:
    print("Your user name can't contain spaces.")
elif not user_name.isalpha():
    print("Your user name can't contain numbers or special characters.")
else:
    print(f"Welcome {user_name}!")
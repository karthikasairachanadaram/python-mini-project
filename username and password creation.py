print(" CREATE ACCOUNT ")

username = input("Enter your username: ")

print("\nPassword must contain:")
print("1. At least 8 characters")
print("2. One uppercase letter")
print("3. One lowercase letter")
print("4. One number")
print("5. One special character")

password = input("\nEnter your password: ")

if len(password) >= 8:
    if any(i.isupper() for i in password):
        if any(i.islower() for i in password):
            if any(i.isdigit() for i in password):
                if any(i in "@#$%&*" for i in password):
                    print("\nAccount created successfully!")
                    print("Username:", username)
                else:
                    print("Password must contain a special character.")
            else:
                print("Password must contain a number.")
        else:
            print("Password must contain a lowercase letter.")
    else:
        print("Password must contain an uppercase letter.")
else:
    print("Password must contain at least 8 characters.")
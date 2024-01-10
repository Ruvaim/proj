#LAB 04
# Create a Python program that reads a file with a list of passwords. The program will check each password to see if it meets specific criteria such as having at least 8 characters, both uppercase and lowercase letters, and at least one number and one special character. If a password meets these requirements, it will be printed by the program.
import re

def validate_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*()])"
    if bool(re.match(pattern,password)):
        print(f"{password} password is valid")
    else:
        print(f"{password} password is invalid")

with open("passwords.txt") as f:
    passwords = f.readlines()
    for password in passwords:
        validate_password(password.strip())
        
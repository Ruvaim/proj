#LAB 03
# Write a Python program to check if a password meets the following criteria: A. Length of at least 8 characters, b. Contains at least one uppercase letter, one lowercase letter, one number, and one special letter. symbol (!, @, #, $, % or &), V. If the password meets the criteria, print a Valid Password message else print “not valid”

import re

def validate_password(password):
    # pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()])(?=.*\d)"
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*()])"
    if bool(re.match(pattern,password)):
        print(f"{password} password is valid")
    else:
        print(f"{password} password is invalid")

password = input("Enter password:")
validate_password(password)
        
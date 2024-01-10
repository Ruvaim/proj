# LAB 02
# Create a Python program that has a function to generate random passwords. The function should have a default length of 8 characters but can also be specified by the user.
import random,string
def generate_password(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
password = generate_password(int(input("Enter password length:") or 8)) 
print("Generated password:", password)
# LAB 01
# . Write a Python program that defines a function and takes a password string as input and returns its SHA-256 hashed representation as a hexadecimal string.
import hashlib
def hash_password():
    return hashlib.sha256(input("Enter password:").encode("utf-8")).hexdigest()
print(f"Hashed password: {hash_password()}")
# LAB 06
# Create a Python program that reads a file with usernames and passwords and checks if each password has been leaked in a data breach the "(https://haveibeenpwned.com/API/v3)" API.
import requests
import hashlib
with open('pass.txt','r') as f:
    for line in f:
        username,password=line.strip().split(',')
        password_hash=hashlib.sha1(password.encode('utf8')).hexdigest().upper()
        response=requests.get(f"https://api.pwnedpasswords.com/range/{password_hash[:5]}")
        if response.status_code==200:
            hashes=[line.split(':')for line in response.text.splitlines()]
            for h,count in hashes:
                if password_hash[5:]==h:
                    print(f"password for user {username} has been leaked{count} times.")
                    break
                else:
                    print(f"could not check password for user {username}.")
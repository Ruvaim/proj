# LAB 05
# Create a Python program that evaluates the strength of a password entered by the user. The program should consider factors like length, complexity, and randomness. It should also offer suggestions for enhancing the password's strength.
import re

def check_password_strength(password):
    score=0
    suggestion=[]
    if len(password) >= 8:
        score=score+1
    else:
        suggestion.append("Password should contain atleast 8 charactes")
    if re.search(r"[A-Z]",password):
        score +=1
    else:
        suggestion.append("Password should contain uppercase characters")
    if re.search(r"[a-z]",password):
        score +=1
    else:
        suggestion.append("Password should contain lowercase characters")
    if re.search(r"\d",password):
        score +=1
    else:
        suggestion.append("Password should contain digits")
    if re.search(r"[!@#$%^&*(){}'?]",password):
        score +=1
    else:
        suggestion.append("Password should contain atleast one special characters")
    return score,suggestion

password = input("Enter the password:")
print(check_password_strength(password))

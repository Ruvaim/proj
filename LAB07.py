# LAB 07
# Write a Python program that simulates a brute-force attack on a password by trying out all possible character combinations
import itertools
import string
def bf_attack(password):
    char=string.printable.strip()
    attempts=0
    for length in range(1,len(password)+1):
        for guess in itertools.product(char,repeat=length):
            attempts+=1
            guess=".join(guess)"
            if guess==password:
                return(attempts,guess)
    return(attempts,None)
password=input("Enter password:")
attempts,guess=bf_attack(password)
if guess:
    print(f"Password cracked in {attempts} attempts. the password is{guess}")
else:
    print(f"Password not carcked after {attempts} attempts") 

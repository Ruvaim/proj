# LAB 09
# Python program implementation for hacking Caesar cipher algorithm

message = "AISA NAKKO KARO"
for key in range(26):
    decrypted = ""
    for letter in message:
        if letter.isalpha():
            shifted = chr((ord(letter) - key - 65) % 26 + 65)
            decrypted += shifted
        else:
            decrypted += letter
print(f"Key #{key}: {decrypted}")


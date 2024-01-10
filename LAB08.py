# LAB 08
# . Python program for implementation symmetric encryption using Caesar cipher algorithm
def ceasae_cipher(text,shift):
    encription_text=""
    for char in text:
        if char.isalpha():
            encription_text += chr(ord(char)+shift)
        else:
            encription_text += char
    return encription_text

text = input("Enter the text:")
shift = 3
print(f"Encrypted text is: {ceasae_cipher(text,shift)}")
# LAB 11
# Python program for encoding and decoding using Base64
import base64

def base64_encode(text):
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")

def base64_decode(encoded_text):
    return base64.b64decode(encoded_text.encode("utf-8")).decode("utf-8")

textToEncode = "Hello world"
encodedText=base64_encode(textToEncode)
print("Encoded Text:",encodedText)
decodedText=base64_decode(encodedText)
print("Decoded Text:",decodedText)

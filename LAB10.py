# LAB 10
# Python program to implement asymmetric encryption using RSA python library


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)

pubKey=keyPair.publickey()
pubKeyPEM=pubKey.exportKey()
privKeyPEM=keyPair.exportKey()

msg=b'Welcome to AIMCA'
encrypted=PKCS1_OAEP.new(pubKey).encrypt(msg)
print("Encrypted:",binascii.hexlify(encrypted))

decrypted=PKCS1_OAEP.new(keyPair).decrypt(encrypted)
print("Decrypted:",decrypted.decode('utf-8'))



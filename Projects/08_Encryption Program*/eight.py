# Encryption Program
# Encryption is the process of converting readable data (plaintext) into an unreadable format (ciphertext) 
# to protect it from unauthorized access.

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

#ENCRYPT
plain_txt = input("Enter a message to encrypt: ")
cipher_txt = ""

for letter in plain_txt:
    index = chars.index(letter)
    cipher_txt += key[index]

print(f"Original message : {plain_txt}")     # I like pizza
print(f"Encrypted message : {cipher_txt}")   # <p@>Z pa>EEu


#DECRYPT
cipher_txt = input("Enter a message to encrypt: ")
plain_txt = ""

for letter in cipher_txt:
    index = key.index(letter)
    plain_txt += chars[index]

print(f"Encrypted message : {cipher_txt}")  # <p@>Z pa>EEu
print(f"Original message : {plain_txt}")    # I like pizza
  
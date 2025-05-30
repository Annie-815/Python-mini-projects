import string
import random

chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)
keys = chars.copy()

# print(f"characters {chars}")
# print(f"keys {keys}")

random.shuffle(keys)

#encryprion
plain = input("Enter a message to enrypt: ")
cipher = ''
for letter in plain:
    index = chars.index(letter)
    cipher += keys[index]
print(f"original message {plain}")
print(f"Encrypted message {cipher}")
#decryption
cipher = input("enter a message to decrypt: ")
plain = ''
for letter in cipher:
    index = keys.index(letter)
    plain += chars[index]

print(f"Encrypted message {cipher}")
print(f"original message {plain}")

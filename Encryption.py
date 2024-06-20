alphabet = "abcdefghijklnmopqrstuvwxyz"
key = 4
character = input ("please enter a character to encrypt")
position = alphabet.find(character)
newposition = (position + key) % 26
encryptedLetter = alphabet[newposition]
print ("your encrypted letter is" , encryptedLetter)

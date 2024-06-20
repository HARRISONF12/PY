alphabet = "abcdefghijklmnopqrstuvwxyz"
message = input ("please select a message to decrypt").lower()
encryptedMessage = ""
key = input ("please enter the keys ")
key = int (key)
for char in message:
    if char in alphabet:
        position = alphabet.find(char)
        newPosition = (position + key) % 26
        encryptedMessage = encryptedMessage + alphabet[newPosition]
    else:
        encryptedMessage = encryptedMessage + char
print ("your encrypted message is:" , encryptedMessage)

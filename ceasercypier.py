#ask the user for the message to encrypt
message = (input("What is your message?"))

# Ask the user for the number of positions to shift
shift = int(input("How many positions do you want to shift."))

#create an empty string to hold the encrypted message
encrypted_message = ""

# Loop through each character in the message
for i in message:
    #shift the character by the shift amount and wrap around using modulo 26
    shifted = (ord(i) - ord('A') + shift) %  26
    # convert the shifted numeric value back to a character and directly add to the string
    encrypted_message += chr(shifted + ord('A'))
    
print(encrypted_message)

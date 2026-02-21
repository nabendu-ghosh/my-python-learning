alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_message = ""
    for letter in original_text:
        start_index = alphabet.index(letter)
        new_index = start_index + shift_amount
        if new_index < 26:
            shifted_letter = alphabet[new_index]
        else:
            shifted_letter = alphabet[new_index - 26]
        encrypted_message += shifted_letter
    print(f"Your encoded message:\t {encrypted_message}")

def decrypt(encrypted_text, shift_amount):
    decrypted_message = ""
    for letter in encrypted_text:
        start_index = alphabet.index(letter)
        new_index = start_index - shift_amount
        if new_index > 0:
            shifted_letter = alphabet[new_index]
        else:
            shifted_letter = alphabet[new_index + 26]
        decrypted_message += shifted_letter
    print(f"Your decoded message:\t {decrypted_message}")
    
if action == "encode":
    encrypt(message, shift)
elif action == "decode":
    decrypt(message, shift)
else:
    print("You have typed wrong input")

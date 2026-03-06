alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

run_again = "YES"

def encrypt(original_text, shift_amount):
    encrypted_message = ""
    for letter in original_text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) + shift_amount) % 26
            encrypted_message += alphabet[new_index]
        else:
            encrypted_message += letter

    print(f"Your encoded message:\t {encrypted_message}")

def decrypt(encrypted_text, shift_amount):
    decrypted_message = ""
    for letter in encrypted_text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) - shift_amount) % 26
            decrypted_message += alphabet[new_index]
        else:
            decrypted_message += letter
    print(f"Your decoded message:\t {decrypted_message}")

while run_again == "YES":

    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = str(input("Type your message:\n")).lower()
    shift = int(input("Type the shift number:\n"))

    if action == "encode":
        encrypt(message, shift)
    elif action == "decode":
        decrypt(message, shift)
    else:
        print("You have typed wrong input")
    
    run_again = input("Type \"Yes\" to go again or \"No\" to exit:\t").upper()

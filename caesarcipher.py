letters = "abcdefghijklmnopqrstuvxyz"
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext.lower():
        if letter in letters:
            position = letters.find(letter)
            new_position = (position + key) % num_letters
            ciphertext += letters[new_position]
        elif letter == " ":
            ciphertext += " "
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext.lower():
        if letter in letters:
            position = letters.find(letter)
            new_position = (position - key) % num_letters
            plaintext += letters[new_position]
        elif letter == " ":
            plaintext += " "
    return plaintext

print("***   CAESAR CIPHER PROGRAM   ***\n")
print("Choose 'e' for ENCRYPTION or 'd' for DECRYPTION\n")

mode = input("e/d: ").lower()
print()

if mode == "e":
    print("ENCRYPTION MODE\n")
    plaintext = input("Enter the text to encrypt: ")
    key = int(input("Enter the encryption key: "))
    result = encrypt(plaintext, key)
    print(f"Encrypted text: {result}")

elif mode == "d":
    print("DECRYPTION MODE\n")
    ciphertext = input("Enter the text to decrypt: ")
    key = int(input("Enter the decryption key: "))
    result = decrypt(ciphertext, key)
    print(f"Decrypted text: {result}")

else:
    print("Invalid option. Please choose 'e' or 'd'.")



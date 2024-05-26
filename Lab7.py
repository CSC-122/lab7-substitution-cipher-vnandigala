# CSC 122
# Substitution Cipher
# By <Your Name>

"""
Inputs, Processes, Outputs (IOP)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""


def encrypt_message(message):
    encrypted_message = ""
    for char in message:
        encrypted_message += chr(ord(char) + 3)
    return encrypted_message


def decrypt_message(cipher):
    decrypted_message = ""
    for char in cipher:
        decrypted_message += chr(ord(char) - 3)
    return decrypted_message


def main():
    message = input("Enter the message to be encrypted: ")
    encrypted_message = encrypt_message(message)
    print(f"Encrypted message = {encrypted_message}\n")

    cipher = input("Enter the cipher to be decrypted: ")
    decrypted_message = decrypt_message(cipher)
    print(f"Decrypted message = {decrypted_message}\n")


if __name__ == "__main__":
    main()

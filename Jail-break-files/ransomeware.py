import os
import cryptography
from cryptography.fernet import Fernet

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

def walk_path(path, key, operation):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            operation(file_path, key)

password = input("Enter your password: ")
key = cryptography.fernet.Fernet.generate_key()
encrypt_path = '/path/to/encrypt'
decrypt_path = '/path/to/decrypt'

walk_path(encrypt_path, key, encrypt)
walk_path(decrypt_path, key, decrypt)

print("Files have been encrypted with the key " + str(key))

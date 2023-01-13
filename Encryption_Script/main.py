import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import time

def encrypt(message, password):
    # Generate a key from the password
    salt = b'\x0c\xed\xd6\x8c\x9e\xaa\x1e\x1d\x96\x99\xee\x8d\xd4\x9e\x9c\xa4'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))

    # Encrypt the message
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())

    return encrypted_message

def decrypt(encrypted_message, password):
    # Generate the key from the password
    salt = b'\x0c\xed\xd6\x8c\x9e\xaa\x1e\x1d\x96\x99\xee\x8d\xd4\x9e\x9c\xa4'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))

    # Decrypt the message
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()

    return decrypted_message

def encrypt_and_decrypt():
    message = input("Enter the message to encrypt: ")
    password = input("Enter the key to encrypt the message: ")
    print("Encrypting message...")
    start = time.time()
    encrypted_message = encrypt(message, password)
    end = time.time()
    print("Encryption time:", end - start)
    print("Encrypted message:", encrypted_message)
    print("Decrypting message...")
    start = time.time()
    decrypted_message = decrypt(encrypted_message, password)
    end = time.time()
    print("Decryption time:", end - start)
    print("Decrypted message:", decrypted_message)

encrypt_and_decrypt()

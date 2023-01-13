import time

def encrypt(plaintext, key):
    """Encrypts plaintext using a Caesar cipher with the given key"""
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord(char) + key
            if char.isupper():
                if shift > ord('Z'):
                    shift -= 26
                final_char = chr(shift)
            else:
                if shift > ord('z'):
                    shift -= 26
                final_char = chr(shift)
            ciphertext += final_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    """Decrypts ciphertext using a Caesar cipher with the given key"""
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord(char) - key
            if char.isupper():
                if shift < ord('A'):
                    shift += 26
                final_char = chr(shift)
            else:
                if shift < ord('a'):
                    shift += 26
                final_char = chr(shift)
            plaintext += final_char
        else:
            plaintext += char
    return plaintext

def main():
    message = input("Enter a message to encrypt: ")
    key = int(input("Enter a key (1-26): "))
    start_time = time.time()
    encrypted_message = encrypt(message, key)
    encrypt_time = time.time() - start_time
    print(f"Encrypted message: {encrypted_message}")
    print(f"Encryption time: {encrypt_time} seconds")
    start_time = time.time()
    decrypted_message = decrypt(encrypted_message, key)
    decrypt_time = time.time() - start_time
    print(f"Decrypted message: {decrypted_message}")
    print(f"Decryption time: {decrypt_time} seconds")

if __name__ == "__main__":
    main()

import time

def encrypt_ottendorf(message, key):
    """Encrypt a message using the Ottendorf Cipher and a key (text)"""
    key_index = 0
    encrypted_message = ""
    key = key.lower()
    for char in message:
        if char.isalpha():
            char_index = ord(char) - ord('a')
            key_char = key[key_index % len(key)]
            key_char_index = ord(key_char) - ord('a')
            encrypted_char = chr((char_index + key_char_index) % 26 + ord('a'))
            key_index += 1
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt_ottendorf(encrypted_message, key):
    """Decrypt an encrypted message using the Ottendorf Cipher and a key (text)"""
    key_index = 0
    decrypted_message = ""
    key = key.lower()
    for char in encrypted_message:
        if char.isalpha():
            char_index = ord(char) - ord('a')
            key_char = key[key_index % len(key)]
            key_char_index = ord(key_char) - ord('a')
            decrypted_char = chr((char_index - key_char_index) % 26 + ord('a'))
            key_index += 1
        else:
            decrypted_char = char
        decrypted_message += decrypted_char
    return decrypted_message

# Take message from user
message = input("Enter a message to encrypt: ")

# Use a pre-arranged key
key = input("Enter the key (text): ")

# Encrypt the message
start_time = time.time()
encrypted_message = encrypt_ottendorf(message, key)
print("Encrypted message: ", encrypted_message)

# Decrypt the message
decrypted_message = decrypt_ottendorf(encrypted_message, key)
end_time = time.time()
print("Decrypted message: ", decrypted_message)

# Print the time taken to decrypt the message
print("Time taken to decrypt the message: ", end_time - start_time)

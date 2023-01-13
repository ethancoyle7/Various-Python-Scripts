import time

def encrypt(key, message):
    matrix = create_matrix(key)
    message = prepare_message(message)
    encrypted_message = ""
    for i in range(0, len(message), 2):
        pair = message[i:i+2]
        encrypted_pair = encrypt_pair(matrix, pair)
        encrypted_message += encrypted_pair
    return encrypted_message

def decrypt(key, encrypted_message):
    matrix = create_matrix(key)
    decrypted_message = ""
    for i in range(0, len(encrypted_message), 2):
        pair = encrypted_message[i:i+2]
        decrypted_pair = decrypt_pair(matrix, pair)
        decrypted_message += decrypted_pair
    return decrypted_message

def create_matrix(key):
    matrix = []
    for i in range(5):
        matrix.append([0] * 5)
    letters = list(key)
    letters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    i, j = 0, 0
    for letter in letters:
        if letter not in matrix[i]:
            matrix[i][j] = letter
            j += 1
            if j == 5:
                j = 0
                i += 1
    return matrix

def encrypt_pair(matrix, pair):
    x1, y1, x2, y2 = get_coordinates(matrix, pair)
    if x1 == x2:
        y1 = (y1 + 1) % 5
        y2 = (y2 + 1) % 5
    elif y1 == y2:
        x1 = (x1 + 1) % 5
        x2 = (x2 + 1) % 5
    else:
        x1, y1, x2, y2 = y1, x2, y1, x2
    return matrix[x1][y1] + matrix[x2][y2]

def decrypt_pair(matrix, pair):
    x1, y1, x2, y2 = get_coordinates(matrix, pair)
    if x1 == x2:
        y1 = (y1 - 1) % 5
        y2 = (y2 - 1) % 5
    elif y1 == y2:
        x1 = (x1 - 1) % 5
        x2 = (x2 - 1) % 5
    else:
        x1, y1, x2, y2 = y1, x2, y1, x2
    return matrix[x1][y1] + matrix[x2][y2]
# This function takes in two arguments, the matrix and a pair of letters. It loops through the matrix using two nested loops, checking if the current element is equal to either letter of the pair. If it is, it assigns the coordinates of that element to the appropriate variables (x1, y1 or x2, y2). At the end of the function, it returns the coordinates of the two letters in the pair as a tuple (x1, y1, x2, y2).
# This function is called by the encrypt_pair and decrypt_pair functions in the code snippet to get the coordinates of the letters in the pair and use them for encryption and decryption process.
  def get_coordinates(matrix, pair):
    x1, y1, x2, y2 = 0, 0, 0, 0
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == pair[0]:
                x1, y1 = i, j
            if matrix[i][j] == pair[1]:
                x2, y2 = i, j
    return x1, y1, x2, y2
  def prepare_message(message):
    message = message.replace(" ", "")
    message = message.upper()
    message = filter_repeated_letters(message)
    if len(message) % 2 != 0:
        message += "X"
    return message

def filter_repeated_letters(message):
    filtered_message = ""
    for i in range(len(message)):
        if i == 0 or message[i] != message[i-1]:
            filtered_message += message[i]
    return filtered_message

def encrypt_message():
    key = input("Enter the key for the Playfair Cipher: ")
    message = input("Enter the message to be encrypted: ")
    start_time = time.time()
    encrypted_message = encrypt(key, message)
    end_time = time.time()
    print("Encrypted message: ", encrypted_message)
    print("Encryption time: ", end_time - start_time, " seconds")

encrypt_message()

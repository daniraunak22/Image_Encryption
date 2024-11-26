"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
     Encodes the binary message into the image by altering the least significant bits of the pixel values.

Assignment Information:
    Assignment:     tp2 task 3
    Team ID:        LC5 - 13 
    Author:         Rohan Shah, shah1091@purdue.edu; Raunak Dani, dani@purdue.edu, Timothy Jiang, jian1046@purude.edu, Faricio Giusti Oliveira Monteiro, fgiustio@purdue.edu
    Date:           10/08/2024

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""
"""
from PIL import Image
import numpy as np

def vigenere_encrypt(text, key):
    # List to store the encrypted characters
    converted = []
    
    # Define the alphabet and digit sets
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    
    # Get the length of the key for repeating it
    key_length = len(key)
    
    # Convert the key into a list that is shifted, for example A=0, B=1, ...
    key_shifts = [alphabet_upper.index(char.upper()) for char in key]
    
    # Encrypt each character in the text
    for i in range(len(text)):
        char = text[i]
        shift = key_shifts[i % key_length]
        
        # Check if the character is an uppercase letter
        if char in alphabet_upper:
            index = alphabet_upper.index(char)
            new_index = (index + shift) % 26
            encrypted_char = alphabet_upper[new_index]
        
        # Check if the character is a lowercase letter
        elif char in alphabet_lower:
            index = alphabet_lower.index(char)
            new_index = (index + shift) % 26
            encrypted_char = alphabet_lower[new_index]
        
        # Check if the character is a digit
        elif char in digits:
            index = digits.index(char)
            new_index = (index + shift % 10) % 10
            encrypted_char = digits[new_index]
        
        # Leave non-alphabetic and non-numeric characters unchanged
        else:
            encrypted_char = char
        
        converted.append(encrypted_char)
    
    # Combines the list to a string, which can be returned at the end of the function
    return ''.join(converted)

def string_to_binary(string):
    return ''.join(format(ord(char), '08b') for char in string)

def encode_message_in_image(binary_message, input_image_path, output_image_path):
    image = Image.open(input_image_path)
    image = image.convert('RGB')
    pixels = np.array(image, dtype=np.uint8)

    binary_index = 0
    for row in range(pixels.shape[0]):
        for col in range(pixels.shape[1]):
            for channel in range(3):  # R, G, B
                if binary_index < len(binary_message):
                    pixel_value = pixels[row, col, channel]
                    new_pixel_value = (pixel_value & 0xFE) | int(binary_message[binary_index])
                    pixels[row, col, channel] = new_pixel_value
                    binary_index += 1

    encoded_image = Image.fromarray(pixels, 'RGB')
    encoded_image.save(output_image_path)
    print(f"Message successfully encoded and saved to: {output_image_path}")

def main():
    plaintext = input("Enter the plaintext you want to encrypt: ")
    key = input("Enter the key for Vigenere cipher: ")
    start_sequence = input("Enter the start sequence: ")
    end_sequence = input("Enter the end sequence: ")
    input_image_path = input("Enter the path of the image: ")
    output_image_path = input("Enter the path for the encoded image: ")

    encrypted_message = vigenere_encrypt(plaintext, key)
    print(f"Encrypted Message using Vigenere Cipher: {encrypted_message}")

    full_message = start_sequence + encrypted_message + end_sequence
    binary_message = string_to_binary(full_message)
    print(f"Binary output message: {binary_message}")

    encode_message_in_image(binary_message, input_image_path, output_image_path)

if __name__ == "__main__":
    main()
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def encrypt(plaintext, key):
    ciphertext = []
    key_length = len(key)
    key_index = 0
    numbers = "0123456789"

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % key_length].upper()) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext.append(encrypted_char)
            key_index += 1
        elif char in numbers:
            shift = (int(char) + ord(key[key_index % key_length].upper()) - ord('A')) % 10
            ciphertext.append(str(shift))
            key_index += 1
        else:
            ciphertext.append(char)
            key_index += 1

    return ''.join(ciphertext)

def to_binary_string(start_sequence, message, end_sequence):
    start_binary = ' '.join(format(ord(char), '08b') for char in start_sequence)
    message_binary = ' '.join(format(ord(char), '08b') for char in message)
    end_binary = ' '.join(format(ord(char), '08b') for char in end_sequence)

    return f"{start_binary} {message_binary} {end_binary}"

def encode_image(binary_message, input_image_path, output_image_path):
    binary_list = list(''.join(binary_message.split()))

    image = Image.open(input_image_path)
    image_data = np.array(image)

    if len(binary_list) > image_data.size:
        return

    binary_index = 0
    if len(image_data.shape) == 3:  # Color image (RGB)
        for row in range(image_data.shape[0]):
            for col in range(image_data.shape[1]):
                for channel in range(image_data.shape[2]):
                    if binary_index < len(binary_list):
                        image_data[row, col, channel] = (image_data[row, col, channel] & 0xFE) | int(binary_list[binary_index])
                        binary_index += 1
                    else:
                        break
                if binary_index >= len(binary_list):
                    break
            if binary_index >= len(binary_list):
                break
    elif len(image_data.shape) == 2:  # Grayscale image
        for row in range(image_data.shape[0]):
            for col in range(image_data.shape[1]):
                if binary_index < len(binary_list):
                    image_data[row, col] = (image_data[row, col] & 0xFE) | int(binary_list[binary_index])
                    binary_index += 1
                else:
                    break
            if binary_index >= len(binary_list):
                break

    output_image = Image.fromarray(image_data)
    output_image.save(output_image_path)
    print(f"Message successfully encoded and saved to: {output_image_path}")

    plt.imshow(image_data, cmap='gray' if len(image_data.shape) == 2 else None)
    plt.axis('off')
    plt.show()

def main():
    plaintext = input("Enter the plaintext you want to encrypt: ")
    key = input("Enter the key for Vigenere cipher: ")
    start_sequence = input("Enter the start sequence: ")
    end_sequence = input("Enter the end sequence: ")
    input_image_path = input("Enter the path of the image: ")
    output_image_path = input("Enter the path for the encoded image: ")

    ciphertext = encrypt(plaintext, key)
    print(f"Encrypted Message using Vigenere Cipher: {ciphertext}")

    binary_message = to_binary_string(start_sequence, ciphertext, end_sequence)
    print(f"Binary output message: {binary_message}")

    encode_image(binary_message, input_image_path, output_image_path)

if __name__ == "__main__":
    main()

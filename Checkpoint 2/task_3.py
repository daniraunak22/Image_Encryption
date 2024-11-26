"""
Description:
     Encodes the binary message into the image by altering the least significant bits of the pixel values.
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


"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Uncover a concealed binary message in an image using the LSB method.


Assignment Information:
    Assignment:     11.1.1 Demo Task 2
    Team ID:        LC5-13
    Author:         Rohan Shah, shah1091@purdue.edu; Raunak Dani, dani@purdue.edu, Timothy Jiang, jian1046@purude.edu, Fabricio Giusti Oliveira Monteiro, fgiustio@purdue.edu
    Date:           10/16/2024

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
import numpy as np
import matplotlib.pyplot as plt

def image(file_name):
    #Reusing the same code from Checkpoint 1 Task 1 to read the image and convert it to an array
    image = plt.imread(file_name)
    image_array = np.array(image)
    if image_array.dtype != np.uint8:
        image_array = (image_array * 255).astype(np.uint8)
    #New code that indexes the 3D array to extract the last bit of every bite
    total_binary = []
    #Accounting for both 2D and 3D arrays depending on if the image is colored or greyscale
    if len(image_array.shape) == 3:
        #Index 3 total times to get the 8th bit of colored image
        for i in range(image_array.shape[0]):
            for j in range(image_array.shape[1]):
                for k in range(image_array.shape[2]):
                    total_binary.append(image_array[i, j, k] & 1)
    elif len(image_array.shape) == 2:
        #Index 2 total times to get the 8th bit of greyscale image
        for i in range(image_array.shape[0]):
            for j in range(image_array.shape[1]):
                total_binary.append(image_array[i, j] & 1) 
    return total_binary

def convert_input(input_text):
    #Found on stack overflow https://stackoverflow.com/questions/18815820/how-to-convert-string-to-binary
    input_bi = ''.join(format(ord(i), '08b') for i in input_text)
    return input_bi

def extract(image_bi, start, end):
    #Converts each element of binary_data to a string and then concentrates them into a single binary string 
    binary_string = ''.join(map(str, image_bi))

    #find the start binary code inside the string
    start_index = binary_string.find(start)
    #find the end binary code inside the string
    end_index = binary_string.find(end, start_index + len(start))
    #if the start and end binary code are inside the string
    if start_index != -1 and end_index != -1:
        start_index += len(start)
        hidden_message = binary_string[start_index:end_index]
        print("Extracted Binary Message: ", hidden_message)
    #if it cannot find the start or the end point inside the string
    else:
        print("Start or end sequence not found in image.")
        return False
    return hidden_message

# Function to convert a binary string to text
def binary_to_text(binary):
    # Convert every 8 bits (1 byte) of the binary string to a character
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

# Function to decrypt a Caesar cipher given a shift value
def caesar_decrypt(ciphertext, shift):
    shift = int(shift) % 26  # Ensure the shift is within the range of the alphabet (0-25)
    plaintext = ""  # Initialize an empty string for the decrypted text
    # Loop through each character in the ciphertext
    for char in ciphertext:
        if char.isalpha():  # Only decrypt alphabetic characters
            # Determine if the character is uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Shift the character back by the given shift value
            plaintext += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            # Non-alphabetic characters remain unchanged
            plaintext += char 
    return plaintext  # Return the decrypted text

# Function to decrypt using XOR cipher with a repeating key
def xor_decrypt(ciphertext, key):
    # Loop through the ciphertext and XOR each character with the corresponding character in the key
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(ciphertext))

# Function to decrypt a Vigenère cipher given a key
def vigenere_decrypt(ciphertext, key):
    key = key.upper()  # Ensure the key is uppercase
    key_length = len(key)  # Get the length of the key
    key_int = [ord(i) for i in key]  # Convert key characters to integers (ASCII values)
    plaintext = []  # Initialize an empty list for the decrypted text

    # Loop through each character in the ciphertext
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():  # Only decrypt alphabetic characters
            # Determine if the character is uppercase or lowercase
            offset = 65 if ciphertext[i].isupper() else 97
            c = ord(ciphertext[i].upper()) - 65  # Convert character to a number (A=0, B=1, etc.)
            k = key_int[i % key_length] - 65  # Get corresponding key character and convert to a number
            # Decrypt the character and append it to the plaintext list
            decrypted_char = chr((c - k) % 26 + offset)
            plaintext.append(decrypted_char.lower() if ciphertext[i].islower() else decrypted_char)
        elif ciphertext[i].isdigit():  # Decrypt numeric characters (optional enhancement)
            c = int(ciphertext[i])
            k = key_int[i % key_length] - 65  # Use modulo 10 for numbers
            decrypted_char = str((c - (k % 10)) % 10)
            plaintext.append(decrypted_char)
        else:
            # Non-alphabetic and non-numeric characters remain unchanged
            plaintext.append(ciphertext[i])
    return ''.join(plaintext)  # Return the decrypted text as a string

# Main function to coordinate the extraction and decryption process
def main():
    # Prompt user for decryption method, key, start and end sequences, and image path
    cipher = input("Enter the cipher you want to use for encryption: ")
    key = input("Enter the key for the cipher: ")
    start_sequence = input("Enter the start sequence: ")
    end_sequence = input("Enter the end sequence: ")
    input_image = input("Enter the path of the input image: ")

    # Extract the binary message from the image
    image_bi = image(input_image)
    start_bi = convert_input(start_sequence)
    end_bi =convert_input(end_sequence)

    # Convert the extracted binary message to text (ciphertext)
    message_bi = extract(image_bi,start_bi,end_bi)
    if message_bi == False:
        return
    else:
        ciphertext = binary_to_text(message_bi)
    # Determine which decryption method to use based on user input
        if cipher == 'caesar':
            plaintext = caesar_decrypt(ciphertext, key)
        elif cipher == 'xor':
            plaintext = xor_decrypt(ciphertext, key)
        elif cipher == 'vigenere':
            plaintext = vigenere_decrypt(ciphertext, key)

    # Print the results: binary message, ciphertext, and decrypted plaintext
        print(f"Converted Binary Text: {ciphertext}")
        print(f"Converted text: {plaintext}")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
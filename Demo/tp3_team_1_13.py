"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    The purpose of this assignment is ask a user for a cipher, input text, and the key to encrypt the text. 
    Once the message is encrypted, then it is converted to binary, then inputted into the image that is desired,
    and then compared against test cases to display the 2 individual images. Then a 3rd iamge that displays the 
    differences betwen teh first two.

Assignment Information:
    Assignment:     11.1.1 Demo Task 1
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

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def input_to_bi(input): #Transform the string into binary code
    return ''.join(format(ord(c), '08b') for c in input)

def bi_to_text(bi):
    return ''.join(chr(int(bi[i:i+8], 2)) for i in range(0, len(bi), 8))
    # Convert a binary string (sequence of '0' and '1') into a text string
    # The binary string is split into chunks of 8 bits (1 byte), and each byte is converted into a character using chr()

def xor_cipher(plain_txt, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(plain_txt))

    # Perform XOR encryption/decryption on the given plaintext using the provided key
    # Each character in the plaintext is XORed with the corresponding character from the key
    # The key is repeated cyclically to match the length of the plaintext

def caesar_cipher(plain_txt, key):
    shift = int(key) % 26 #converts value to a 0-26 scale for the caesar cipher
    result = "" #initiliazes empty string
    for char in plain_txt:
        if char.isalpha(): #if the character is an alphabet
            ascii_offset = ord('A') if char.isupper() else ord('a') #checks if the character is upper or lower case, and then sets the offset based on that
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            #Shifts the character by the given amount (wrapping within the alphabet as needed), and converts it back to a character, adding it to the final encrypted string (result).
        else:
            result += char #just adds the result to the code without shifting it as it isnt an alphabet
    return result
  

def vigenere_cipher(plain_txt, key):
    key = key.upper() #changes the key to all uppercase letters
    result = "" #initializes an empty string
    key_index = 0 #starts index at 0
    for char in plain_txt: #loops through every character in the text for encryption
        if char.isalpha(): #if the character is an alphabet
            ascii_offset = ord('A') if char.isupper() else ord('a') #the offset is either 65 (A) or 97(a), depending on if the letter is upper/lower case.
                #This sets the value of the character = 0, so that we go in a range of 0-26
            shift = ord(key[key_index % len(key)]) - ord('A')
            #Cycles the key over and over again to match the charactes. From here, it subtracts the letter matching the key index with A, to find the total shift
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            #this then uses the total shift found above along with the character given to then output the new encrypted message into a string.
            key_index += 1
        else:
            result += char #adds the character if it is not an alphabet by not shifting it
    return result

def encode_image(input_image, output_image, bi_message, offset):
    # Convert the image to RGB and then convert into an array
    img = Image.open(input_image).convert("RGB")
    img_array = np.array(img)
    # Calculate the total number of bits and see if the message length exceeds the total number of bits 
    total_bits = img_array.size * 8
    if (offset + len(bi_message)) > total_bits:
        raise ValueError("Given message is too long to be encoded in the image.")
    # Convert binary into a list of characters
    binary_sequence = list(bi_message)
    bin_index = 0
    bit_count = 0

    # Iterate over each pixel in the image array
    for i in np.ndindex(img_array.shape[:-1]):
        # Once the bit count reaches the bit offset, start encoding the message.
        if bit_count >= offset and bin_index < len(binary_sequence):
            # Iterate over the RGB channels of each pixel.
            for channel in range(img_array.shape[2]):
                # For each channel, modify the LSB with the current binary message bit.
                if bin_index < len(binary_sequence):
                    img_array[i][channel] &= 0XFE
                    img_array[i][channel] |= int(binary_sequence[bin_index])
                    bin_index += 1  # Move to the next bit in the binary message.
        bit_count += 3 # Increment the bit count by 3
        if bin_index >= len(binary_sequence):
            break
    # Convert the array back into an image and save to output file
    encoded_img = Image.fromarray(img_array)
    encoded_img.save(output_image)

def compare_images(image1_path, image2_path, output_path):
    #Converting both images to RGB
    image1 = Image.open(image1_path).convert("RGB")
    image2 = Image.open(image2_path).convert("RGB")
    # Check if images are the same size
    if image1.size != image2.size:
        raise ValueError("Images must have the same size")
    # Turning the images into arrays
    img1_array = np.array(image1)
    img2_array = np.array(image2)
    # Calculate the absolute difference between the two image arrays
    diff_array = np.abs(img1_array.astype(np.float32) - img2_array.astype(np.float32))
    #Convert difference array into 8bit and create an image from the difference
    diff_image = Image.fromarray(diff_array.astype(np.uint8))
    # Save the image to the output file
    diff_image.save(output_path)
    # Create three subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    # Display original image
    ax1.imshow(image1)
    ax1.set_title("Original Image")
    ax1.axis('off')
    # Display encoded image
    ax2.imshow(image2)
    ax2.set_title("Encoded Image")
    ax2.axis('off')
    # Display the difference between the two images
    ax3.imshow(diff_image)
    ax3.set_title("Difference")
    ax3.axis('off')

    plt.tight_layout()
    plt.show()

    return np.array_equal(img1_array, img2_array)

def main():
    # Obtain inputs from the user
    cipher_choice = input("Enter the cipher you want to use for encryption: ")
    plain_txt = input("Enter the plaintext you want to encrypt: ")
    key = input("Enter the key for the cipher: ")
    start = input("Enter the start sequence: ")
    end = input("Enter the end sequence: ")
    offset = int(input("Enter the bit offset before you want to start encoding: "))
    input_image = input("Enter the path of the input image: ")
    output_image = input("Enter the path for your encoded image: ")
    compare_image = input("Enter the path of the image you want to compare: ")

    # Determine which cipher is being used
    if cipher_choice == "xor":
        encrypted_message = xor_cipher(plain_txt, key)
        name_cipher = "Xor"
    elif cipher_choice == "caesar":
        encrypted_message = caesar_cipher(plain_txt, int(key))
        name_cipher = "Caesar"
    elif cipher_choice == "vigenere":
        encrypted_message = vigenere_cipher(plain_txt, key)
        name_cipher = "Vigenere"

    # Print the encrypted message as a string
    print(f"Encrypted Message using {name_cipher} Cipher: {encrypted_message}")
    # Convert the message to a binary string and print as groups of 8 bits
    start_bi = input_to_bi(start)
    end_bi = input_to_bi(end)
    encrypted_message = input_to_bi(encrypted_message)
    bi_message = start_bi + encrypted_message + end_bi
    print(f"Binary output message: {bi_message}")

    # Encode the encrypted message into the input image and save to the output file 
    encode_image(input_image, output_image, bi_message, offset)
    print(f"Message successfully encoded and saved to: {output_image}")
    # Compare the output image with another image and save the differences to an output file
    images_identical = compare_images(output_image, compare_image, "diff_image.png")
    if images_identical:
        print("The images are the same.")
    else:
        print("The images are different.")

if __name__ == "__main__":
    main()
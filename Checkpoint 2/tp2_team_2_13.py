"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Uses the Vigenère cipher to encrypt a string. Specifically, a word can be entered, and then encrypted using a key word. This shifts the indexes, outputting an encrypted word.

Assignment Information:
    Assignment:     tp2 task 2
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

def string_to_binary(message, start_seq, end_seq):
    # Convert a string to its binary representation using ASCII values
    def to_binary(s):
        return ' '.join(format(ord(char), '08b') for char in s)
    
    # Get binary forms of the sequences and the message
    start_bin = to_binary(start_seq)
    message_bin = to_binary(message)
    end_bin = to_binary(end_seq)
    
    # Combine them with spaces in between
    return start_bin + ' ' + message_bin + ' ' + end_bin

def main():
    # Get user inputs
    text = input("Enter the plaintext message: ")
    key = input("Enter the key: ")
    start = input("Enter the start sequence: ")
    end = input("Enter the end sequence: ")
    
    # Encrypt the message and convert it to binary
    encrypted_message = vigenere_encrypt(text, key)
    binary_message = string_to_binary(encrypted_message, start, end)
    
    # Print the results
    print("Encrypted Message using Vigenere Cipher:", encrypted_message)
    print("Binary output message:", binary_message)

if __name__ == "__main__":
    main()

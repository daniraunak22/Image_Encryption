"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Converts a binary string into ASCII text.

Assignment Information:
    Assignment:     9.2.3 tp1 Team 3
    Team ID:        LC5 - 13
    Author:         Rohan Shah, shah1091@purdue.edu; Raunak Dani, dani@purdue.edu, Timothy Jiang, jian1046@purdue.edu, Fabricio Giusti Oliveira Monteiro, fgiustio@purdue.edu
    Date:           10/01/2024

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
#
def cipher(full_string):
    #uses a conversion table similar to the ashbash cipher used in Py4 individual task 2
    convert_table = {
        '01000001': 'A', '01000010': 'B', '01000011': 'C', '01000100': 'D', '01000101': 'E', '01000110': 'F', '01000111': 'G', '01001000': 'H',
        '01001001': 'I', '01001010': 'J', '01001011': 'K', '01001100': 'L', '01001101': 'M', '01001110': 'N', '01001111': 'O', '01010000': 'P',
        '01010001': 'Q', '01010010': 'R', '01010011': 'S', '01010100': 'T', '01010101': 'U', '01010110': 'V', '01010111': 'W', '01011000': 'X',
        '01011001': 'Y', '01011010': 'Z', '01100001': 'a', '01100010': 'b', '01100011': 'c', '01100100': 'd', '01100101': 'e', '01100110': 'f',
        '01100111': 'g', '01101000': 'h', '01101001': 'i', '01101010': 'j', '01101011': 'k', '01101100': 'l', '01101101': 'm', '01101110': 'n',
        '01101111': 'o', '01110000': 'p', '01110001': 'q', '01110010': 'r', '01110011': 's', '01110100': 't', '01110101': 'u', '01110110': 'v',
        '01110111': 'w', '01111000': 'x', '01111001': 'y', '01111010': 'z', '00100000': ' ', '00101110': '.'
    }
    
    #creates an empty string that stores the new word letter by letter
    encrypted = ''
    #iterates through the inputted binary, splits it into segments of 8, then uses the conversion table to evaluate binary to words, letter by letter
    for i in range(0, len(full_string), 8):
        byte = full_string[i:i+8]
        encrypted += convert_table.get(byte)
    return encrypted

def main():
    #asks for the binary input
    binary_message = input("Enter the binary message: ")
    #calls the cipher function to convert the binary input into a word
    print(f"Converted text: {cipher(binary_message)}")

if __name__ == "__main__":
    main()
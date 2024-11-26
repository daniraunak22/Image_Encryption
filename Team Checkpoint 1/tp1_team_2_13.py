"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Extracts binary data from the LSB of each pixel’s value in an image.

Assignment Information:
    Assignment:     9.2.2 tp1 Team 2
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

#Importing the required libraries
import numpy as np
import matplotlib.pyplot as plt

def image(file_name):
    #Reusing the same code from Task 1 to read the image and convert it to an array
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

#Converting the user input to binary
def convert_input(input_text):
    #Found on stack overflow https://stackoverflow.com/questions/18815820/how-to-convert-string-to-binary
    input_bi = ''.join(format(ord(i), '08b') for i in input_text)
    return input_bi

def extract(file_name, start, end):
    image_binary = image(file_name)
    #Converts each element of binary_data to a string and then concentrates them into a single binary string 
    binary_string = ''.join(map(str, image_binary))

    #find the start binary code inside the string
    start_index = binary_string.find(start)
    #find the end binary code inside the string
    end_index = binary_string.find(end, start_index + len(start))
    #if the start and end binary code are inside the string
    if start_index != -1 and end_index != -1:
        start_index += len(start)
        hidden_message = binary_string[start_index:end_index]
        print("Extracted Message: ", hidden_message)
    #if it cannot find the start or the end point inside the string
    else:
        print("Start or end sequence not found in image.")

def main():
    #Gets the user inputs to use in the code
    image_path = input("Enter the path of the image you want to load: ")
    start = input("Enter the start sequence: ")
    end = input("Enter the end sequence: ")
    #Converting start and end sequence to binary
    start_bi = convert_input(start)
    end_bi = convert_input(end)
    extract(image_path, start_bi, end_bi)
#Ending code
if __name__ == "__main__":
    main()
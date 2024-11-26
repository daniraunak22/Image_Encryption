"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Program that loads a user specified image and prepares it for message extraction.

Assignment Information:
    Assignment:     9.2.1 tp1 Team 1
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
#importing libraries
import matplotlib.pyplot as plt
import numpy as np

#turning image into array
def load_image(file_name):
    image = plt.imread(file_name)
    #image = Image.open(file_name)
    image_array = np.array(image)

    if image_array.dtype == 2 or image_array.dtype == 3:
        image_array = (image_array * 255).astype(np.uint8)
    return image_array
#outputting image
def display_image(image_array): 
    plt.imshow(image_array, cmap='gray' if image_array.ndim == 2 else None)
    plt.axis()  
    plt.show()
#user input the reference file
def main():
    file_name = input("Enter the path of the image you want to load: ")
    image_array = load_image(file_name)
    display_image(image_array)

if __name__ == "__main__":
    main()
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
   #input_int = int(input_text)
    #input_bi = bin(input_int)[2:]
    #return input_bi

def extract(file_name, start, end):
    image_binary = image(file_name)
    #Converts each element of binary_data to a string and then concentrates them into a single binary string 
    binary_string = ''.join(map(str, image_binary))

    #find the start binary code inside the string
    start_index = binary_string.find(start)
    #find the end binary code inside the string
    end_index = binary_string.find(end, start_index + len(start))
    #if the start and end binary code are inside the string
    print(f"Below is the img_array output of {file_name}:")
    if start_index != -1 and end_index != -1:
        start_index += len(start)
        hidden_message = binary_string[start_index:end_index]
        print("Extracted Message:", hidden_message)
    #if it cannot find the start or the end point inside the string
    else:
        return "Start or end sequence not found in image."
    return hidden_message

def cipher(full_string):
    #uses a conversion table similar to the ashbash cipher used in Py4 individual task 2
    convert_table = {
        '01000001': 'A', '01000010': 'B', '01000011': 'C', '01000100': 'D', '01000101': 'E', '01000110': 'F', '01000111': 'G', '01001000': 'H',
        '01001001': 'I', '01001010': 'J', '01001011': 'K', '01001100': 'L', '01001101': 'M', '01001110': 'N', '01001111': 'O', '01010000': 'P',
        '01010001': 'Q', '01010010': 'R', '01010011': 'S', '01010100': 'T', '01010101': 'U', '01010110': 'V', '01010111': 'W', '01011000': 'X',
        '01011001': 'Y', '01011010': 'Z', '01100001': 'a', '01100010': 'b', '01100011': 'c', '01100100': 'd', '01100101': 'e', '01100110': 'f',
        '01100111': 'g', '01101000': 'h', '01101001': 'i', '01101010': 'j', '01101011': 'k', '01101100': 'l', '01101101': 'm', '01101110': 'n',
        '01101111': 'o', '01110000': 'p', '01110001': 'q', '01110010': 'r', '01110011': 's', '01110100': 't', '01110101': 'u', '01110110': 'v',
        '01110111': 'w', '01111000': 'x', '01111001': 'y', '01111010': 'z', '00100000': ' ', '00101110': '.',
        '00110000': '0', '00110001': '1', '00110010': '2', '00110011': '3', '00110100': '4', '00110101': '5',
        '00110110': '6', '00110111': '7', '00111000':'8', '00111001':'9', '00100001':'!'
    }
    #creates an empty string that stores the new word letter by letter
    encrypted = ''
    #iterates through the inputted binary, splits it into segments of 8, then uses the conversion table to evaluate binary to words, letter by letter
    for i in range(0, len(full_string), 8):
        byte = full_string[i:i+8]
        encrypted += convert_table.get(byte)
    return encrypted

def main():
    #Gets the user inputs to use in the code
    image_path = input("Enter the path of the image you want to load: ")
    start = input("Enter the start sequence: ")
    end = input("Enter the end sequence: ")
    #Converting start and end sequence to binary
    start_bi = convert_input(start)
    end_bi = convert_input(end)
    #extract(image_path, start_bi, end_bi)
    result = extract(image_path, start_bi, end_bi)
    if result != "Start or end sequence not found in image.":
        print(f"Converted text: {cipher(result)}")
    else:
        print("Start or end sequence not found in the image.")
#Ending code
if __name__ == "__main__":
    main()

"""
Description:
    Compares two images at the pixel level to determine if a message is encoded in one of them. Depending on the differences at the pixel level, then it outputs a graph displaying the differences.
"""

import numpy as np
import matplotlib.pyplot as plt

def compare_images(image1_filename, image2_filename, output_filename):
    # Load the images
    image_1 = plt.imread(image1_filename)
    image_2 = plt.imread(image2_filename)

    # Ensure both images have the same number of channels
    if image_1.shape[-1] == 4:
        image_1 = image_1[:, :, :3]
    if image_2.shape[-1] == 4:
        image_2 = image_2[:, :, :3]

    # Check if the images are the same size
    if image_1.shape != image_2.shape:
        print("Cannot compare images of different sizes.")
        return False

    # Compare the images
    diff = np.abs(image_1 - image_2)
    if image_1.ndim ==2:
        cmap="grey"
    else:
        cmap=None
    plot_this = np.where(diff > 0, 255, 0).astype(np.uint8)
    
    plt.imsave(output_filename, plot_this)
    if cmap:
        plt.imshow(plot_this, cmap=cmap)
    else:
        plt.imshow(plot_this,)
    plt.show()

    # Determine if there are any differences
    identical = not np.any(diff)
    return identical

def main():
    # Prompt the user for file names
    image_1_file = input("Enter the path of your first image: ")
    image_2_file = input("Enter the path of your second image: ")
    output_file = input("Enter the path for the output image: ")

    # Compare the images
    identical = compare_images(image_1_file, image_2_file, output_file)

    if identical:
        print("The images are the same.")
    else:
        print("The images are different.")

if __name__ == "__main__":
    main()

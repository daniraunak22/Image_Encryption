from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def image_difference(image1_path, image2_path):
    # Open the images
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)

    # Convert images to numpy arrays
    arr1 = np.array(img1)
    arr2 = np.array(img2)

    # Ensure the images have the same size
    if arr1.shape != arr2.shape:
        raise ValueError("Images must have the same dimensions")

    # Calculate the absolute difference
    diff = np.abs(arr1 - arr2)

    # Create an image from the difference array
    diff_image = Image.fromarray(diff.astype(np.uint8))

    # Plot the difference image
    plt.imshow(diff_image)
    plt.show()

# Example usage
image_difference('ref_col.png', 'ref_col_e.png')
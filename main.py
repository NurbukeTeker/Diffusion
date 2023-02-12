import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

def diffuse_image(image, alpha, n_iterations):
    """Diffuse an image using a 2D diffusion model.

    Parameters:
    image -- input image
    alpha -- diffusion coefficient
    n_iterations -- number of iterations

    Returns:
    diffused_image -- diffused image
    """
    # Define the filter for the diffusion process
    filter = np.array([[0, alpha, 0], [alpha, 1 - 4 * alpha, alpha], [0, alpha, 0]])

    # Create a copy of the image
    diffused_image = np.copy(image)

    # Apply the diffusion process
    for i in range(n_iterations):
        diffused_image = ndi.convolve(diffused_image, filter, mode='reflect')

    return diffused_image

# Load the input image
image = plt.imread("input_image.jpg")

# Apply the diffusion model to the image
diffused_image = diffuse_image(image, alpha=0.1, n_iterations=100)

# Plot the input and diffused images
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Input Image")
plt.subplot(1, 2, 2)
plt.imshow(diffused_image)
plt.title("Diffused Image")
plt.show()

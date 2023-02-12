# Diffusion
# Image Diffusion Model

This repository contains code for a 2D diffusion model applied to an image. The diffusion model is implemented using the finite difference method and the `scipy.ndimage` library in Python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following libraries installed in order to run the code:

- `numpy`
- `scipy`
- `matplotlib`

You can install these libraries using the following command:

pip install numpy scipy matplotlib


### Running the Code

To run the code, simply run the following command in the terminal:

python diffusion_model.py


This will apply the diffusion model to an input image and plot the original and diffused images for comparison.

## Customizing the Code

You can change the input image by replacing the `input_image.jpg` file with your own image.

You can also modify the diffusion parameters by changing the `alpha` and `n_iterations` arguments in the `diffuse_image` function. The `alpha` argument is the diffusion coefficient, which controls the amount of diffusion, and the `n_iterations` argument is the number of iterations, which controls the duration of the diffusion process.

## Conclusion

This code serves as a simple example of how to apply a 2D diffusion model to an image using the finite difference method and the `scipy.ndimage` library in Python. Feel free to use and modify the code as you see fit.

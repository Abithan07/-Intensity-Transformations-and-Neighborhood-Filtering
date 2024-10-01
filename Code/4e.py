a = 0.5
sigma = 70

# Generate a range of input pixel vslue ranging from 0 to 255
input_values = np.arange(0, 256)

# Apply the intensity transformation to each pixel
output_values = [vibrance_intensity_transformation(x, a, sigma) for x in input_values]
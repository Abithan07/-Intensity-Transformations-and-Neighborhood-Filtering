def vibrance_intensity_transformation(x, a, sigma=70):
    return np.minimum(x + a * 128 * np.exp(-(x - 128)**2 / (2 * sigma**2)), 255)

# Set a value for a
a = 0.5

# Apply the intensity transformation to the saturation channel
s_transformed = vibrance_intensity_transformation(s.astype(np.float64), a)
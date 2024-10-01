def apply_convolution(image, kernel):
    """Apply a convolution operation using the specified kernel."""
    kernel_h, kernel_w = kernel.shape
    img_h, img_w = image.shape
    output = np.zeros((img_h, img_w))
    
    # Pad the image to handle edge cases
    padded_img = np.pad(image, ((1, 1), (1, 1)), 'constant')
    
    for i in range(1, img_h + 1):
        for j in range(1, img_w + 1):
            region = padded_img[i-1:i+2, j-1:j+2]
            output[i-1, j-1] = np.sum(region * kernel)
    
    return output

def sobel_filter(img):
    """Apply Sobel filter to compute X, Y gradients and their magnitude."""
    # Define Sobel kernels for X and Y direction
    kernel_x = np.array([[1, 0, -1],
                         [2, 0, -2],
                         [1, 0, -1]])
    
    kernel_y = np.array([[1, 2, 1],
                         [0, 0, 0],
                         [-1, -2, -1]])

    # Apply convolution with Sobel kernels
    sobel_x = apply_convolution(img, kernel_x)
    sobel_y = apply_convolution(img, kernel_y)

    # Compute the magnitude of the gradient
    sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    sobel_magnitude = np.clip(sobel_magnitude, 0, 255) 
    
    sobel_x = np.uint8(np.abs(sobel_x))
    sobel_y = np.uint8(np.abs(sobel_y))
    sobel_magnitude = np.uint8(sobel_magnitude)

    return sobel_x, sobel_y, sobel_magnitude
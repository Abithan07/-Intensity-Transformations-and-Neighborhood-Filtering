def sobel_x_filter(image):
    """Apply Sobel X filter for horizontal edge detection."""
    sobel_kernel = np.array([[1, 0, -1],
                             [2, 0, -2],
                             [1, 0, -1]])

    sobel_x_result = np.zeros_like(image, dtype=np.float64)

    padded_image = np.pad(image, ((1, 1), (1, 1)), mode='constant')

    # Convolve with the Sobel kernel
    for x in range(1, padded_image.shape[0] - 1):
        for y in range(1, padded_image.shape[1] - 1):
            region = padded_image[x-1:x+2, y-1:y+2]
            sobel_x_result[x-1, y-1] = np.sum(sobel_kernel * region)

    return np.uint8(np.clip(np.abs(sobel_x_result), 0, 255))
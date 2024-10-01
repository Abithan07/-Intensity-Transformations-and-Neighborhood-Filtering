img_sobel = cv2.imread('a1images/einstein.png', cv2.IMREAD_GRAYSCALE)

# Define the Sobel kernel for x-direction
sobel_kernel_x = np.array([[1, 0, -1],
                           [2, 0, -2],
                           [1, 0, -1]])

# Apply filter2D with the Sobel kernel
sobel_filtered = cv2.filter2D(img_sobel, -1, sobel_kernel_x)
img_flower = cv2.imread('a1images/daisy.jpg')

mask = np.zeros(img_flower.shape[:2], np.uint8)
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)
rect = (50, 100, 600, 500)  # Coordinates for the rectangle

# Apply grabCut algorithm
cv2.grabCut(img_flower, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

# Create binary mask for foreground
mask_foreground = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# Extract the foreground
foreground_img = img_flower * mask_foreground[:, :, np.newaxis]

# Extract the background
background_img = img_flower * (1 - mask_foreground[:, :, np.newaxis])
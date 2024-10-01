_, mask = cv2.threshold(s2, 13, 255, cv2.THRESH_BINARY)  # Adjust the threshold value as needed

# Extract the foreground using the mask
foreground = cv2.bitwise_and(image, image, mask=mask)

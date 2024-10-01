# Apply Gaussian blur to the background
blurred_background = cv2.GaussianBlur(background_img, (63, 63), 0)

# Combine blurred background and the foreground
final_img = blurred_background * (1 - mask_foreground[:, :, np.newaxis]) + foreground_img
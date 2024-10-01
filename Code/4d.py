# Convert back to uint8
s_transformed = np.clip(s_transformed, 0, 255).astype(np.uint8)

# Recombine the HSV channels
hsv_img_transformed = cv2.merge([h, s_transformed, v])

# Convert back to BGR color space
vibrance_enhanced_img = cv2.cvtColor(hsv_img_transformed, cv2.COLOR_HSV2BGR)
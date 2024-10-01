img = cv2.imread('a1images/highlights_and_shadows.jpg')

# Convert the image to L*a*b* color space
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Split L*, a*, and b* channels
L, a, b = cv2.split(lab_img)

# Apply gamma correction to the L channel (assume γ=2.2 for increased gamma and γ=0.5 for decreased gamma)
gamma_H = 2.2
gamma_L = 0.5
L_normalized = L / 255.0
L_gamma_H_corrected = np.power(L_normalized, gamma_H)
L_gamma_H_corrected = (L_gamma_H_corrected * 255).astype(np.uint8)

# Merge back the channels and convert to BGR
lab_img_corrected_H = cv2.merge([L_gamma_H_corrected, a, b])
gamma_H_corrected_img = cv2.cvtColor(lab_img_corrected_H, cv2.COLOR_LAB2BGR)

L_gamma_L_corrected = np.power(L_normalized, gamma_L)
L_gamma_L_corrected = (L_gamma_L_corrected * 255).astype(np.uint8)

# Merge back the channels and convert to BGR
lab_img_corrected_L = cv2.merge([L_gamma_L_corrected, a, b])
gamma_L_corrected_img = cv2.cvtColor(lab_img_corrected_L, cv2.COLOR_LAB2BGR)

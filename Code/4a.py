img_vibrance = cv2.imread('a1images/spider.png')

# Convert the image to HSV color space
hsv_img = cv2.cvtColor(img_vibrance, cv2.COLOR_BGR2HSV)

# Split the channels
h, s, v = cv2.split(hsv_img)
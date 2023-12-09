import numpy as np
import cv2

image = cv2.imread("../assets/color_wheel.png", -1)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_blue = np.array([[[90, 40, 40]]])
upper_blue = np.array([[[130, 255, 255]]])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Color Detection", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

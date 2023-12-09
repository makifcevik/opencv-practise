import cv2
import numpy as np

image1 = np.array([220, 45, 145], dtype=np.uint8)
image2 = np.array([200, 60, 100], dtype=np.uint8)

result_pixel = cv2.bitwise_and(image1, image2)
print(result_pixel)

"""

11011100  # Binary representation of 220
11001000  # Binary representation of 200
--------
11001000  # Result of bitwise AND which corresponds to 200

00101101  # Binary representation of 45
00111100  # Binary representation of 60
--------
00101100  # Result of bitwise AND which corresponds to 44

10010001  # Binary representation of 145
01100100  # Binary representation of 100
--------
00000000  # Result of bitwise AND which corresponds to 0

"""
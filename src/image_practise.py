import numpy as np
import cv2
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
img_path = os.path.join(script_dir, "../assets/chessboard.png")
img = cv2.imread(img_path)

# horizontal lines
for i in range(10):
    for j in range(img.shape[1]):
        img[i][j] = [0, 255, 255]
        img[-i][j] = [0, 255, 255]

# vertical lines
for i in range(img.shape[0]):
    for j in range(10):
        img[i][j] = [0, 255, 255]
        img[i][-j] = [0, 255, 255]

# tag = img[100:200, 250:450]
# img[400:500, 50:250] = tag

img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
cv2.imshow("Board", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

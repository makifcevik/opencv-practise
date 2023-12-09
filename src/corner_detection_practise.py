import numpy as np
import cv2

image = cv2.imread("../assets/chessboard.png")
image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(image, 200, 0.1, 50)
# <source><maxCorners><qualityLevel><minDistance>
corners = np.int64(corners)
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (x, y), radius=5, color=[50, 50, 255], thickness=-1)
# print(corners)

cv2.imshow("Board", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

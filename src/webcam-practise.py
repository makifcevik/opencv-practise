import numpy as np
import cv2

# 0 is the index of the cam
cap = cv2.VideoCapture(0)
# width = int(cap.get(3))
# height = int(cap.get(4))
width = 400
height = 400

while True:
    # ret is for if smt goes wrong
    ret, frame = cap.read()
    frame = cv2.resize(frame, (400, 400))
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image = np.zeros(frame.shape, np.uint8)

    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_90_CLOCKWISE)  # top-left
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_90_COUNTERCLOCKWISE)  # top-right
    image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # bottom-left
    image[height//2:, width//2:] = smaller_frame  # bottom-right

    cv2.imshow("Video", image)

    if cv2.waitKey(1) == ord("q"):
        break

# release the camera
cap.release()
cv2.destroyAllWindows()

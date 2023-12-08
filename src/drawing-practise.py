import numpy as np
import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(3))
height = int(cap.get(4))


def draw_line(img, start: tuple, end: tuple, color: tuple = (0, 0, 0), thickness: int = 1):
    return cv2.line(img, start, end, color, thickness)


while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)
    # frame = cv2.line(frame, (0, 0), (width, height), (0, 225, 255), 10)
    frame = draw_line(frame, (0, 0), (width, height))
    frame = cv2.rectangle(frame, (200, 300), (500, 450), (200, 50, 50), -1)
    frame = cv2.circle(frame, (50, 50), 20, (60, 20, 200), -1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "SOME TEXT", (200, 200), font, 1, (0, 0, 0), 10, cv2.LINE_AA)

    cv2.imshow("Live Webcam Video", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

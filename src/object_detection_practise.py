import cv2

image = cv2.imread("../assets/soccer_practice.jpg", 0)
image = cv2.resize(image, (0, 0), fx=.6, fy=.6)
template = cv2.resize(cv2.imread("../assets/ball.png", 0), (0, 0), fx=.6, fy=.6)
template2 = cv2.resize(cv2.imread("../assets/shoe.png", 0), (0, 0), fx=.6, fy=.6)

height, width = template.shape
height2, width2 = template2.shape

result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
result2 = cv2.matchTemplate(image, template2, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)
# print(min_val, max_val, min_loc, max_loc)
cv2.rectangle(image, (max_loc[0] + width, max_loc[1] + height), max_loc, color=[255, 255, 255], thickness=1)
cv2.rectangle(image, max_loc2, (max_loc2[0] + width, max_loc2[1] + height2), color=[255, 255, 255], thickness=1)

cv2.imshow("Soccer", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

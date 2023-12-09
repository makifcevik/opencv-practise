import cv2

img = cv2.imread("../assets/flower.png", -1)

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

tag = img[100:200, 250:450]
img[400:500, 50:250] = tag

cv2.imshow("Flower", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

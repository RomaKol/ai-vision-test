import cv2

img = cv2.imread("images/duck.jpg")

# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img)

img1 = cv2.merge([r, g, b])

# cv2.imshow("Result", img)
cv2.imshow("Result", img1)
cv2.waitKey(0)

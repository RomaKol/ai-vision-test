import cv2
import numpy as np

photo = cv2.imread("images/duck.jpg")
img = np.zeros(photo.shape[:2], dtype='uint8')
# img = np.zeros((350, 350), dtype='uint8')

circle = cv2.circle(img.copy(), (330, 130), 100, 255, thickness=cv2.FILLED)
square = cv2.rectangle(img.copy(), (25, 25), (250, 250), 255, -1)

img = cv2.bitwise_and(photo, photo, mask=circle)
# img = cv2.bitwise_or(circle, square)
# img = cv2.bitwise_xor(circle, square)
# img = cv2.bitwise_not(square)

cv2.imshow("Result", img)
cv2.waitKey(0)

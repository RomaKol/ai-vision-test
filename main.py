import cv2
import numpy as np

# IMAGE
img = cv2.imread('images/duck.jpg')
resized_img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
blurred_img = cv2.GaussianBlur(img, (9, 9), 0)
black_white_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# convert img to lines - binary, number - precisions
angles_img = cv2.Canny(black_white_img, 250, 250)
# matrix for bolder lines
kernel = np.ones((5, 5), np.uint8)
# bolder lines
angles_img = cv2.dilate(angles_img, kernel, iterations=1)
# decrease line width
angles_img = cv2.erode(angles_img, kernel, iterations=1)

# for cutting by pixels use img[0:100, 0:150]
cv2.imshow('image1', angles_img)
# print(img.shape)
cv2.waitKey(5000)

# VIDEO
# video from file
# cap = cv2.VideoCapture('videos/file_example.mp4')
# video from camera
# cap = cv2.VideoCapture(0)
# cap.set(3, 500)
# cap.set(4, 300)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('res', img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

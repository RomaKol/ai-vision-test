import cv2
import numpy as np

img = cv2.imread("images/duck.jpg")
new_img = np.zeros(img.shape, dtype='uint8')

# img = cv2.flip(img, -1)


def rotate(img_param, angle):
    height, width = img_param.shape[:2]
    point = (width // 2, height // 2)
    matrix = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img_param, matrix, (width, height))


# img = rotate(img, 90)


def transform(img_param, del_x, del_y):
    matrix = np.float32([[1, 0, del_x], [0, 1, del_y]])
    return cv2.warpAffine(img_param, matrix, (img_param.shape[1], img_param.shape[0]))


# img = transform(img, 30, 200)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.Canny(img, 100, 140)
contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(new_img, contours, -1, (100, 140, 200), thickness=1)

cv2.imshow("Result", new_img)
cv2.waitKey(0)

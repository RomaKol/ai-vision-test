import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl

img = cv2.imread('images/auto-1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(img_filter, 30, 200)

contours_from_img = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_from_img = imutils.grab_contours(contours_from_img)
contours_from_img = sorted(contours_from_img, key=cv2.contourArea, reverse=True)[:8]

position_of_contour = None
for c in contours_from_img:
    approx = cv2.approxPolyDP(c, 10, True)
    if len(approx) == 4:
        position_of_contour = approx
        break

# print(position_of_contour)

mask = np.zeros(gray.shape, dtype=np.uint8)
new_img = cv2.drawContours(mask, [position_of_contour], 0, 255, -1)
bitwise_img = cv2.bitwise_and(img, img, mask=mask)

(x, y) = np.where(mask == 255)
(x1, y1) = np.min(x), np.min(y)
(x2, y2) = np.max(x), np.max(y)

cropped_img = gray[x1:x2, y1:y2]

text = easyocr.Reader(['en'])
text = text.readtext(cropped_img)

print(text)

res_number = text[0][-2]
final_img = cv2.putText(img, res_number, (x1 - 90, y2 + 10), cv2.FONT_HERSHEY_PLAIN, 2, (105, 201, 119), 3)
final_img = cv2.rectangle(img, (y1, x1), (y2, x2), (105, 201, 119), 3)

pl.imshow(cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB))
pl.show()

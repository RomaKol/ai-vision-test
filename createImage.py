import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')

# RGB - standart
# BGR - format for OpenCV
# photo[:] = 105, 201, 119
# photo[100:150, 200:280] = 0, 0, 255
cv2.rectangle(photo, (50, 50), (100, 100), (105, 201, 119), thickness=3)
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (105, 201, 119), thickness=3)
cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (105, 201, 119), thickness=cv2.FILLED)
cv2.putText(photo, 'photoText', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), thickness=1)

cv2.imshow('Photo', photo)
cv2.waitKey(0)

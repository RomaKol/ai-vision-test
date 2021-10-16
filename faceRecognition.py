import cv2

img = cv2.imread('images/faces-2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('faces.xml')

results = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (105, 201, 119), thickness=3)

cv2.imshow("Faces", img)
cv2.waitKey(0)

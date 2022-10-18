import cv2

# Load image, convert to grayscale, Otsu's threshold
image = cv2.imread('C1.PNG')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Find contours, obtain bounding rect, and draw width
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)

    cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 23)

cv2.imshow('image', image)
cv2.waitKey()